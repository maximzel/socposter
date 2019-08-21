from django.db import models
from django.db.models.signals import pre_save
from rsser.parser import get_data_for_twitter
from rsser.api_tl import main_tl
from rsser.api_vk import main_vk
from rsser.api_fb import main_fb
from rsser.api_tw import main_tw


class Rss(models.Model):
    rss_text_fb = models.TextField('text_fb', null=True, blank=True)
    rss_text_tw = models.CharField('text_tw', max_length=257, null=True, blank=True)
    is_parse_text_tw = models.BooleanField('есть текст для tw? (не парсить текст?)', default=False)
    rss_link = models.CharField('link', max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    is_teleg = models.BooleanField('не слать в Telegram?', default=False)
    is_vk = models.BooleanField('не слать в Вконтакте?', default=False)
    is_fb = models.BooleanField('не слать в Facebook?', default=False)
    is_tw = models.BooleanField('не слать в Twitter?', default=False)
    rss_image_tw = models.CharField('image link', max_length=200, null=True, blank=True)
    is_parse_image_tw = models.BooleanField('есть ссылка на картинку? (не парсить картинку?)', default=False)


class Autoparsed(models.Model):
    rss_link = models.CharField('link', max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)


def switch_executer(instance, *args, **kwargs):
    rss_link = instance.rss_link
    rss_text_fb = instance.rss_text_fb
    rss_text_tw = instance.rss_text_tw
    rss_image_tw = instance.rss_image_tw
    data_for_twitter = get_data_for_twitter(rss_link)
    if not instance.is_parse_image_tw:
        rss_image_tw = data_for_twitter['image']
    if not instance.is_parse_text_tw:
        rss_text_tw = data_for_twitter['heading']
    if not instance.is_teleg:
        main_tl(rss_text_fb, rss_link)
    if not instance.is_vk:
        main_vk(rss_text_fb, rss_link)
    if not instance.is_fb:
        main_fb(rss_text_fb, rss_link)
    if not instance.is_tw:
        main_tw(rss_text_tw, rss_link, rss_image_tw)


pre_save.connect(switch_executer, sender=Rss, weak=True, dispatch_uid=None)
