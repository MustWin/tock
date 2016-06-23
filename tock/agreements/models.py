from django.db import models
from client.models import Client

# Create your models here.

class AgreementAuthority(models.Model):
    authority_short_title = models.CharField(help_text="i.e. 'Economy Act'", verbose_name="Short Title", max_length=500)
    statutory_citation = models.CharField(help_text="i.e. '31 USC 1535'", max_length=500)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Agreement Authority"
        verbose_name_plural = "Agreement Authorities"

    def __str__(self):
        return '%s' % (self.authority_short_title)


class GenTermCond(models.Model):
    client = models.ForeignKey(Client, blank=True, null=True)
    agreement_id = models.CharField(blank=True, verbose_name="Agreement ID", max_length=200)
    assisted_acq = models.BooleanField(default=False, help_text="7600A, Block 3", verbose_name="Assisted acquisition?")
    doc_url = models.URLField(verbose_name = "URL of 7600A General Terms & Conditions", blank=True)
    gtc_start = models.DateField(blank=True, null=True, verbose_name="7600A Period of Performance Start", help_text="7600A, Block 5")
    gtc_end = models.DateField(blank=True, null=True, verbose_name="7600A Period of Performance End", help_text="7600A, Block 5")
    estimate_direct = models.DecimalField(null=True, max_digits=100, decimal_places=2)
    estimate_overhead = models.DecimalField(null=True, max_digits=100, decimal_places=2)
    estimate_total = models.DecimalField(null=True, max_digits=100, decimal_places=2) #TODO: automatically add gtc_estimate_direct and gtc_estimate_overhead to get this total.
    requesting_agency_authority = models.ForeignKey(AgreementAuthority, verbose_name="Requesting Agency's (Client's) Authority", help_text="7600A, Block 10a", null=True)
    requesting_agency_authority = models.ForeignKey(AgreementAuthority, verbose_name="Servicing Agency's Authority", help_text="7600A, Block 10b", null=True)
    approval_date = models.DateField(blank=True, verbose_name="7600A Date Signed", null=True)

    class Meta:
        verbose_name = "7600A - General Terms & Conditions"
        verbose_name_plural = "7600As - General Terms & Conditions"

    def __str__(self):
        return '%s - %s, (%s - %s)'  % (self.client, self.agreement_id, self.gtc_start, self.gtc_end)

class OrderReqFundInfo(models.Model):
    is_modification = models.BooleanField(default=False, verbose_name="Check if modification") #TODO Turn this into a prompt that directs the user to the "Modification" model.
    gen_term_cond = models.ForeignKey(GenTermCond, verbose_name="Associated 7600A", null=True)
    pop_start = models.DateField(verbose_name="Period of Performance Start", blank=True, null=True)
    pop_end = models.DateField(verbose_name="Period of Performance End", blank=True, null=True)

    class Meta:
        verbose_name = "7600B - Order Requirements and Funding Information"
        verbose_name_plural = "7600Bs - Order Requirements and Funding Information"

class ModOrderReqFundInfo(models.Model):
    mod_target = models.ForeignKey(OrderReqFundInfo, null=True)

    class Meta:
        verbose_name = "7600B Modification"
        verbose_name_plural = "7600B Modifications"
