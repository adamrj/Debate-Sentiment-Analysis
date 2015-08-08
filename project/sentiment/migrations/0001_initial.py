# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('query_string', models.CharField(max_length=200)),
                ('candidate', models.CharField(max_length=200)),
            ],
        ),
    ]
