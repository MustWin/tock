# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20160623_0548'),
        ('agreements', '0002_auto_20160623_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='gentermcond',
            name='agency',
            field=models.ForeignKey(to='client.ClientAgency', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='gentermcond',
            name='agreement_id',
            field=models.CharField(blank=True, max_length=200, verbose_name='Agreement ID'),
        ),
        migrations.AddField(
            model_name='gentermcond',
            name='approval_date',
            field=models.DateField(blank=True, null=True, verbose_name='7600A Date Signed'),
        ),
        migrations.AddField(
            model_name='gentermcond',
            name='requesting_agency_authority',
            field=models.ForeignKey(verbose_name="Servicing Agency's Authority", help_text='7600A, Block 10b', to='agreements.AgreementAuthority', null=True),
        ),
        migrations.AddField(
            model_name='orderreqfundinfo',
            name='gen_term_cond',
            field=models.ForeignKey(to='agreements.GenTermCond'),
        ),
    ]
