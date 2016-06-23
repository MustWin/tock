# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20160623_0502'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAgency',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Agency List',
                'verbose_name': 'Agency List',
            },
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': 'Clients', 'verbose_name': 'Client'},
        ),
        migrations.AlterField(
            model_name='client',
            name='agency_name',
            field=models.ForeignKey(to='client.ClientAgency', verbose_name='Agency Name'),
        ),
        migrations.DeleteModel(
            name='Agency',
        ),
        migrations.AddField(
            model_name='clientagency',
            name='agency_name',
            field=models.ForeignKey(to='projects.Agency'),
        ),
    ]
