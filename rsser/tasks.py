from __future__ import absolute_import, unicode_literals
from celery import shared_task
from rsser.utilities import parse_and_post_rss_data


@shared_task
def parse_rss_and_post():
    parse_and_post_rss_data()
