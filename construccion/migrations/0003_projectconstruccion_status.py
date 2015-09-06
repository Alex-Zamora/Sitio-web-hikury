# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construccion', '0002_auto_20150825_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectconstruccion',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
