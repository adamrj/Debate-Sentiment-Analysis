# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('word', models.CharField(db_index=True, max_length=150)),
                ('positive', models.IntegerField()),
                ('negative', models.IntegerField()),
            ],
        ),
    ]
