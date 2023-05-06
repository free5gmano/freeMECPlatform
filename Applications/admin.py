from django.contrib import admin
from Applications.models import *
# Register your models here.
admin.site.register(DnsRule)
admin.site.register(TrafficRule)
admin.site.register(TrafficFilter)
admin.site.register(DstInterface)