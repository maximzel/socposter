# Generated by Django 2.0.7 on 2018-08-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsser', '0009_auto_20180808_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rss',
            name='is_tiw',
        ),
        migrations.AddField(
            model_name='rss',
            name='is_tw',
            field=models.BooleanField(default=False, verbose_name='Twitter?'),
        ),
    ]
