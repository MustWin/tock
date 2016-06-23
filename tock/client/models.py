from django.db import models
from projects.models import Agency

# Create your models here.

class Client(models.Model):
    """ Stores Client information """
    agency_name = models.ForeignKey(Agency, null=True, verbose_name="Agency Name", help_text="7600A, Block 1")
    office = models.CharField(max_length=200, verbose_name = "Office Name", help_text="7600A, Block 1")
    phyiscal_address = models.TextField(max_length=500, verbose_name = "Client Address", help_text = "7600A, Block 1")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return '%s' % (self.agency_name)
