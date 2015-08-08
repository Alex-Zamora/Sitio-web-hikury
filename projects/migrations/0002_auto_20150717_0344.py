# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 17, 3, 44, 4, 965214, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='categorys',
            field=models.ManyToManyField(to='blog.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='technologys',
            field=models.ManyToManyField(to='projects.Technology'),
            preserve_default=True,
        ),
    ]
