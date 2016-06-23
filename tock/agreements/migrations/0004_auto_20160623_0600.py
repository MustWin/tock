# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20160623_0548'),
        ('agreements', '0003_auto_20160623_0548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gentermcond',
            name='agency',
        ),
        migrations.AddField(
            model_name='gentermcond',
            name='client',
            field=models.ForeignKey(to='client.Client', null=True, blank=True),
        ),
    ]
