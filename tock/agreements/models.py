from django.db import models

# Create your models here.

class GenTermCond(model.Models):
    assisted_acq = models.BooleanField(default=False, help_text="7600A, Block 3", verbose_name="Assisted acquisition?")
    gtc_link = models.URLField(verbose_name = "URL of 7600A General Terms & Conditions", blank=True)
    gtc_pop_start = models.DateField(blank=True, null=True, verbose_name="7600A Period of Performance Start", help_text="7600A, Block 5")
    gtc_pop_end = models.DateField(blank=True, null=True, verbose_name="7600A Period of Performance End", help_text="7600A, Block 5")
    gtc_estimate_direct = models.DecimalField(null=True, max_digits=100, decimal_places=2)
    gtc_estimate_overhead = models.DecimalField(null=True, max_digits=100, decimal_places=2)
    gtc_estimate_total = models.DecimalField(null=True, max_digits=100, decimal_places=2) #TODO: automatically add gtc_estimate_direct and gtc_estimate_overhead to get this total.
#    requesting_agency_authority = models.ForeignKey(client.Client.AgreementAuthority, verbose_name="Requesting Agency's (Client's) Authority", help_text="7600A, Block 10a")
#    requesting_agency_authority = models.ForeignKey(client.Client.AgreementAuthority, verbose_name="Servicing Agency's Authority", help_text="7600A, Block 10b")
    gtc_approval_date
