# Generated by Django 2.0.7 on 2018-08-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsser', '0011_auto_20180808_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rss_text_fb', models.TextField(blank=True, null=True, verbose_name='text_fb')),
                ('rss_text_tw', models.CharField(blank=True, max_length=257, null=True, verbose_name='text_tw')),
                ('rss_link', models.CharField(max_length=200, verbose_name='link')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('is_teleg', models.BooleanField(default=False, verbose_name='Telegram?')),
                ('is_vk', models.BooleanField(default=False, verbose_name='Вконтакте?')),
                ('is_fb', models.BooleanField(default=False, verbose_name='Facebook?')),
                ('is_tw', models.BooleanField(default=False, verbose_name='Twitter?')),
                ('rss_image_tw', models.CharField(blank=True, max_length=200, null=True, verbose_name='image link')),
            ],
        ),
        migrations.RemoveField(
            model_name='switches',
            name='switch',
        ),
        migrations.RemoveField(
            model_name='switchmatching',
            name='switch',
        ),
        migrations.RemoveField(
            model_name='switchmatching',
            name='text',
        ),
        migrations.DeleteModel(
            name='Switches',
        ),
        migrations.DeleteModel(
            name='SwitchMatching',
        ),
        migrations.DeleteModel(
            name='Texts',
        ),
    ]
