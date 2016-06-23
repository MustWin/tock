from django.db import models
import projects

# Create your models here.

class Agency(models.Model):
    agency_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"

    def __str__(self):
        return '%s' % (self.name)

class AgreementAuthority(models.Model):
    authority_short_title = models.CharField(help_text="i.e. 'Economy Act'", verbose_name="Short Title")
    statutory_citation = models.CharField(help_text="i.e. '31 USC 1535'")
    notes = models.TextField()

class Client(models.Model):
    """ Stores Client information """
    agency_name = models.ForeignKey(Agency.agency_name, verbose_name = "Agency Name")
    office = models.CharField(max_length=200, verbose_name = "Office Name")
    phyiscal_address = models.TextField(max_length=500, verbose_name = "Client Address", help_text = "7600A, Block 1")
    name = models.CharField(
        max_length=200,
        verbose_name="Name",
        help_text="Don't make crappy names!")

    class Meta:
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"

    def __str__(self):
        return '%s' % (self.name)
