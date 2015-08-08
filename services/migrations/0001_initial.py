# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='service/')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='service/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
