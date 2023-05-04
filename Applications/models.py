from django.db import models

# Create your models here.
class DnsRule(models.Model):
    appInstanceId = models.CharField(max_length=64, default='unverified')
    dnsRuleId = models.CharField(max_length=64, default='unverified')
    domainName = models.CharField(max_length=64, default='unverified')
    ipAddressType = models.CharField(max_length=64, default='unverified')
    ipAddress = models.CharField(max_length=64, default='unverified')
    ttl = models.CharField(max_length=64, default='unverified')
    state = models.CharField(max_length=64, default='unverified')

class TrafficRule(models.Model):
    appInstanceId = models.CharField(max_length=64, default='unverified')
    trafficRuleId = models.CharField(max_length=64, default='unverified')
    filterType = models.CharField(max_length=64, default='unverified')
    priority = models.CharField(max_length=64, default='unverified')
    trafficFilter = models.CharField(max_length=64, default='unverified')
    action = models.CharField(max_length=64, default='unverified')
    dstInterface = models.CharField(max_length=64, default='unverified')
    state = models.CharField(max_length=64, default='unverified')

class AppTerminationNotificationSubscription(models.Model):
    appInstanceId = models.CharField(max_length=64, default='unverified')
    subscriptionType = models.CharField(max_length=64, default='unverified')
    callbackReference = models.CharField(max_length=64, default='unverified')
    _links = models.CharField(max_length=64, default='unverified')
    self_referring_URI = models.CharField(max_length=64, default='unverified')