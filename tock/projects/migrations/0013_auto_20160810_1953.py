# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20160705_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='aggregate_hours_logged',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='max_hours_restriction',
            field=models.BooleanField(default=False),
        ),
    ]
