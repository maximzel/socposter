# Generated by Django 2.0.7 on 2018-08-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsser', '0005_auto_20180802_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='rss',
            name='rss_image_tw',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='link'),
        ),
    ]