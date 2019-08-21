import requests
from socposter.settings import IFTTT_WEBHOOK_TW_URL


def main_tw(maintext, mainurl, imgurl):
    requests.post(IFTTT_WEBHOOK_TW_URL, data={
        'value1': maintext + ' ' + mainurl,
        'value2': imgurl
        })
