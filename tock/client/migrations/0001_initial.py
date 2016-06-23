# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('agency_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Agency',
                'verbose_name_plural': 'Agencies',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('office', models.CharField(verbose_name='Office Name', max_length=200)),
                ('phyiscal_address', models.TextField(verbose_name='Client Address', help_text='7600A, Block 1', max_length=500)),
                ('name', models.CharField(verbose_name='Name', help_text="Don't make crappy names!", max_length=200)),
                ('agency_name', models.ForeignKey(verbose_name='Agency Name', to='client.Agency')),
            ],
            options={
                'verbose_name': 'Agency',
                'verbose_name_plural': 'Agencies',
            },
        ),
    ]
