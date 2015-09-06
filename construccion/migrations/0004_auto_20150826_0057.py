# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construccion', '0003_projectconstruccion_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectconstruccion',
            name='fecha',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectconstruccion',
            name='link',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
