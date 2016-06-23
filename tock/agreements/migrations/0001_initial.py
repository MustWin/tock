# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgreementAuthority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('authority_short_title', models.CharField(verbose_name='Short Title', help_text="i.e. 'Economy Act'", max_length=500)),
                ('statutory_citation', models.CharField(help_text="i.e. '31 USC 1535'", max_length=500)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GenTermCond',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('assisted_acq', models.BooleanField(verbose_name='Assisted acquisition?', help_text='7600A, Block 3', default=False)),
                ('gtc_link', models.URLField(verbose_name='URL of 7600A General Terms & Conditions', blank=True)),
                ('gtc_pop_start', models.DateField(verbose_name='7600A Period of Performance Start', help_text='7600A, Block 5', blank=True, null=True)),
                ('gtc_pop_end', models.DateField(verbose_name='7600A Period of Performance End', help_text='7600A, Block 5', blank=True, null=True)),
                ('gtc_estimate_direct', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('gtc_estimate_overhead', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('gtc_estimate_total', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
            ],
        ),
    ]
