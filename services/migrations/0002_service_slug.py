# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 7, 15, 6, 4, 16, 715213, tzinfo=utc), max_length=255, blank=True),
            preserve_default=False,
        ),
    ]
