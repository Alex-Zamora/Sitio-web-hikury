# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
                ('url', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
