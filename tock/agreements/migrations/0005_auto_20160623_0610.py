# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreements', '0004_auto_20160623_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModOrderReqFundInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
            options={
                'verbose_name': '7600B Modification',
                'verbose_name_plural': '7600B Modifications',
            },
        ),
        migrations.AlterModelOptions(
            name='gentermcond',
            options={'verbose_name': '7600A - General Terms & Conditions', 'verbose_name_plural': '7600As - General Terms & Conditions'},
        ),
        migrations.AlterModelOptions(
            name='orderreqfundinfo',
            options={'verbose_name': '7600B - Order Requirements and Funding Information', 'verbose_name_plural': '7600Bs - Order Requirements and Funding Information'},
        ),
        migrations.AddField(
            model_name='orderreqfundinfo',
            name='pop_end',
            field=models.DateField(verbose_name='Period of Performance End', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='orderreqfundinfo',
            name='pop_start',
            field=models.DateField(verbose_name='Period of Performance Start', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orderreqfundinfo',
            name='gen_term_cond',
            field=models.ForeignKey(to='agreements.GenTermCond', verbose_name='Associated 7600A', null=True),
        ),
        migrations.AlterField(
            model_name='orderreqfundinfo',
            name='is_modification',
            field=models.BooleanField(verbose_name='Check if modification', default=False),
        ),
        migrations.AddField(
            model_name='modorderreqfundinfo',
            name='mod_target',
            field=models.ForeignKey(null=True, to='agreements.OrderReqFundInfo'),
        ),
    ]
