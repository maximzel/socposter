from telebot import TeleBot
from socposter.settings import TL_CHAT_ID, TL_TOKEN


bot = TeleBot(TL_TOKEN)


def main_tl(maintext, mainurl):
    text = maintext + '\n' + mainurl
    bot.send_message(TL_CHAT_ID, text)
