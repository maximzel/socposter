# Generated by Django 2.0.7 on 2018-08-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsser', '0006_rss_rss_image_tw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rss',
            name='is_parser',
            field=models.BooleanField(default=False, verbose_name='парсить fb?'),
        ),
        migrations.AlterField(
            model_name='rss',
            name='rss_image_tw',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='image link'),
        ),
    ]