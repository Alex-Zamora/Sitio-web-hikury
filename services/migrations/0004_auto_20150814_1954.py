# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20150717_0327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': 'Servicios'},
        ),
    ]
