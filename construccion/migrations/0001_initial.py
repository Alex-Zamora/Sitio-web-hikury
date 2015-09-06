# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectConstruccion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('link', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='construccion/')),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'En construccion',
            },
            bases=(models.Model,),
        ),
    ]
