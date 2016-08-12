# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='max_hours',
            field=models.DecimalField(decimal_places=2, blank=True, null=True, default=0.0, help_text='When set and "Limit to maximum hours" is checked, this project will deactivate when this ceiling is reached.', verbose_name='Maximum hour ceiling', max_digits=10),
        ),
    ]
