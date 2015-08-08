# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image_index', models.ImageField(upload_to='home/')),
                ('title_index', models.CharField(max_length=100)),
                ('logo_menu', models.ImageField(upload_to='home/')),
                ('telephone', models.CharField(max_length=50)),
                ('movil', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
