import requests
from socposter.settings import IFTTT_WEBHOOK_FB_URL


def main_fb(maintext, mainurl):
    requests.post(IFTTT_WEBHOOK_FB_URL, data={
        'value1': maintext + '\n' + mainurl,
        'value2': mainurl
        })
