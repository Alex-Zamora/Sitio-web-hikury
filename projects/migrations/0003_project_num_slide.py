# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150717_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='num_slide',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
