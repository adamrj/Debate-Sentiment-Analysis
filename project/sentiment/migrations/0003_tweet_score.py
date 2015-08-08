# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0002_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='score',
            field=models.DecimalField(default=0.5, decimal_places=5, max_digits=6),
        ),
    ]
