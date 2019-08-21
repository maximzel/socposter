import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    img = soup.find("link", {"rel": "image_src"})['href']
    head = soup.find('h1').text
    output = {'image': img, 'heading': head}
    return output


def get_data_for_twitter(url):
    return get_data(get_html(url))
