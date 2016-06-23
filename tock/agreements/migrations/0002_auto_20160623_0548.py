# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderReqFundInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_modification', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '7600B - Order Requirements and Funding Information',
                'verbose_name': '7600B - Order Requirements and Funding Information',
            },
        ),
        migrations.AlterModelOptions(
            name='agreementauthority',
            options={'verbose_name_plural': 'Agreement Authorities', 'verbose_name': 'Agreement Authority'},
        ),
        migrations.AlterModelOptions(
            name='gentermcond',
            options={'verbose_name_plural': '7600A - General Terms & Conditions', 'verbose_name': '7600A - General Terms & Conditions'},
        ),
        migrations.RenameField(
            model_name='gentermcond',
            old_name='gtc_link',
            new_name='doc_url',
        ),
        migrations.RenameField(
            model_name='gentermcond',
            old_name='gtc_estimate_direct',
            new_name='estimate_direct',
        ),
        migrations.RenameField(
            model_name='gentermcond',
            old_name='gtc_estimate_overhead',
            new_name='estimate_overhead',
        ),
        migrations.RenameField(
            model_name='gentermcond',
            old_name='gtc_estimate_total',
            new_name='estimate_total',
        ),
        migrations.RenameField(
            model_name='gentermcond',
            old_name='gtc_pop_end',
            new_name='gtc_end',
        ),
        migrations.RenameField(
            model_name='gentermcond',
            old_name='gtc_pop_start',
            new_name='gtc_start',
        ),
    ]
