# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20160608_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='assisted_acq',
            field=models.BooleanField(default=False, help_text='7600A, Block 3', verbose_name='Assisted acquisition?'),
        ),
        migrations.AddField(
            model_name='project',
            name='gtc_estimate_direct',
            field=models.DecimalField(null=True, max_digits=100, decimal_places=2),
        ),
        migrations.AddField(
            model_name='project',
            name='gtc_estimate_overhead',
            field=models.DecimalField(null=True, max_digits=100, decimal_places=2),
        ),
        migrations.AddField(
            model_name='project',
            name='gtc_estimate_total',
            field=models.DecimalField(null=True, max_digits=100, decimal_places=2),
        ),
        migrations.AddField(
            model_name='project',
            name='gtc_link',
            field=models.URLField(verbose_name='URL of 7600A General Terms & Conditions', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='gtc_pop_end',
            field=models.DateField(null=True, help_text='7600A, Block 5', verbose_name='7600A Period of Performance End', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='gtc_pop_start',
            field=models.DateField(null=True, help_text='7600A, Block 5', verbose_name='7600A Period of Performance Start', blank=True),
        ),
    ]
