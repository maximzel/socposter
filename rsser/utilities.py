import requests
import time
from requests.exceptions import RetryError, ConnectTimeout, ConnectionError
from bs4 import BeautifulSoup
from socposter.settings import RSS_URL

from rsser.api_tl import main_tl
from rsser.api_vk import main_vk
from rsser.api_fb import main_fb
from rsser.api_tw import main_tw
from rsser.models import Autoparsed


def make_retriable_request(url, retry):
    try:
        response = requests.get(url)
        return response.text
    except (ConnectTimeout, ConnectionError):
        print('connection error, retrying...' + url)
        if retry:
            retry -= 1
            time.sleep(300)
            return make_retriable_request(url, retry=retry)
        raise RetryError


def prepost_checker(img, title, link, description):
    try:
        Autoparsed.objects.get(rss_link=link)
    except Autoparsed.DoesNotExist:
        poster(img=img, title=title, link=link, description=description)
        rss_to_post = Autoparsed(rss_link=link)
        rss_to_post.save()


def poster(img, title, link, description):
    main_tl(maintext=description, mainurl=link)
    main_vk(maintext=description, mainurl=link)
    main_fb(maintext=description, mainurl=link)
    main_tw(maintext=title, mainurl=link, imgurl=img)
    print('Posted: ' + link)
    time.sleep(60)


def parse_and_post_rss_data():
    html_response = make_retriable_request(url=RSS_URL, retry=300)
    soup = BeautifulSoup(html_response, 'xml')
    items = soup.findAll('item')
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        img = item.enclosure['url']
        description_raw = item.find('description').text
        descr = description_raw[description_raw.find(">") + 1:]
        description = BeautifulSoup(descr, 'html.parser').text
        prepost_checker(img=img, title=title, link=link, description=description)
