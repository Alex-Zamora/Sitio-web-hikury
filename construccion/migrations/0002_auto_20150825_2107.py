# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectconstruccion',
            name='fecha',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
