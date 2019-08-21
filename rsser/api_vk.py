import requests
from socposter.settings import VK_GROUP_ID, VK_TOKEN


API_VERSION = 5.52
FRIENDS_ONLY = 0
FROM_GROUP = 1
SIGNED = 0


def main_vk(maintext, mainurl):
    maintext = maintext + '\n' + mainurl
    requests.post('https://api.vk.com/method/wall.post', data={'access_token': VK_TOKEN,
                                                               'owner_id': VK_GROUP_ID,
                                                               'friends_only': FRIENDS_ONLY,
                                                               'from_group': FROM_GROUP,
                                                               'message': maintext,
                                                               'attachments': mainurl,
                                                               'signed': SIGNED,
                                                               'v': API_VERSION,
                                                               })
