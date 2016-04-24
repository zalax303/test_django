# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, verbose_name='\u540d\u5b57')),
                ('desc', models.CharField(max_length=1000, verbose_name='\u63cf\u8ff0')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('manger', models.ForeignKey(verbose_name='\u7ba1\u7406\u5458', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u677f\u5757',
                'verbose_name_plural': '\u677f\u5757',
            },
        ),
    ]
