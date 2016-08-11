# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20160810_1953'),
    ]

    operations = [

        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True, help_text='The active / inactive status of this project is based on the start date, end date, early warning values, maximum hour ceiling, and all time hours logged for this project and cannot be manually set.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='aggregate_hours_logged',
            field=models.DecimalField(verbose_name='All time hours logged', decimal_places=2, help_text='All hours logged by users over all reporting periods.', blank=True, null=True, max_digits=10, default=0.0),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default='If your reading this, a description for this project is missing and should be added.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='max_hours_restriction',
            field=models.BooleanField(verbose_name='Limit to maximum hours', default=False, help_text='Check this to enforce the maximum hours ceiling.'),
        ),
    ]
