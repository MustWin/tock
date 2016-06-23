# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreements', '0004_auto_20160623_0600'),
        ('client', '0002_auto_20160623_0548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientagency',
            name='agency_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='name',
        ),
        migrations.AlterField(
            model_name='client',
            name='agency_name',
            field=models.ForeignKey(verbose_name='Agency Name', to='projects.Agency', null=True, help_text='7600A, Block 1'),
        ),
        migrations.AlterField(
            model_name='client',
            name='office',
            field=models.CharField(verbose_name='Office Name', max_length=200, help_text='7600A, Block 1'),
        ),
        migrations.DeleteModel(
            name='ClientAgency',
        ),
    ]
