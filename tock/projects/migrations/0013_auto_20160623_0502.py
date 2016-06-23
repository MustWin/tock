# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20160623_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='assisted_acq',
        ),
        migrations.RemoveField(
            model_name='project',
            name='gtc_estimate_direct',
        ),
        migrations.RemoveField(
            model_name='project',
            name='gtc_estimate_overhead',
        ),
        migrations.RemoveField(
            model_name='project',
            name='gtc_estimate_total',
        ),
        migrations.RemoveField(
            model_name='project',
            name='gtc_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='gtc_pop_end',
        ),
        migrations.RemoveField(
            model_name='project',
            name='gtc_pop_start',
        ),
    ]
