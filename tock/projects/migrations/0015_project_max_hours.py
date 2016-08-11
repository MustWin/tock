# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160810_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='max_hours',
            field=models.DecimalField(blank=True, verbose_name='Maximum hour ceiling', default=0.0, help_text='When set and "Limit to maximum hours" is checked, this project will deactivate when this ceiling is reached.', decimal_places=2, null=True, max_digits=10),
        ),
    ]
