from django.contrib import admin
from .models import GenTermCond, AgreementAuthority, OrderReqFundInfo, ModOrderReqFundInfo

# Register your models here.

admin.site.register(GenTermCond)
admin.site.register(OrderReqFundInfo)
admin.site.register(AgreementAuthority) #TODO Hide "Agreement Authority" in main Django admin panel.
admin.site.register(ModOrderReqFundInfo)
