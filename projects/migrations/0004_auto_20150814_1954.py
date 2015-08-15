# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_num_slide'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'Tecnologías'},
        ),
    ]
