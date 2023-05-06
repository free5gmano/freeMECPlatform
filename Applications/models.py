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
    trafficFilter_UUID = models.CharField(max_length=64, default='unverified')
    action = models.CharField(max_length=64, default='unverified')
    dstInterface_UUID = models.CharField(max_length=64, default='unverified')
    state = models.CharField(max_length=64, default='unverified')

class TrafficFilter(models.Model):
    trafficFilter_UUID = models.CharField(max_length=64, default='unverified')
    srcAddress = models.CharField(max_length=64, default='unverified')
    dstAddress = models.CharField(max_length=64, default='unverified')
    srcPort = models.CharField(max_length=64, default='unverified')
    dstPort = models.CharField(max_length=64, default='unverified')
    protocol = models.CharField(max_length=64, default='unverified')
    token = models.CharField(max_length=64, default='unverified')
    srcTunnelAddress = models.CharField(max_length=64, default='unverified')
    tgtTunnelAddress = models.CharField(max_length=64, default='unverified')
    srcTunnelPort = models.CharField(max_length=64, default='unverified')
    dstTunnelPort = models.CharField(max_length=64, default='unverified')
    qCI = models.CharField(max_length=64, default='unverified')
    dSCP = models.CharField(max_length=64, default='unverified')
    tC = models.CharField(max_length=64, default='unverified')

class DstInterface(models.Model):
    dstInterface_UUID = models.CharField(max_length=64, default='unverified')
    interfaceType = models.CharField(max_length=64, default='unverified')
    # tunnelInfo start
    tunnelType = models.CharField(max_length=64, default='unverified')
    tunnelDstAddress = models.CharField(max_length=64, default='unverified')
    tunnelSrcAddress = models.CharField(max_length=64, default='unverified')
    # tunnelInfo end
    srcMacAddress = models.CharField(max_length=64, default='unverified')
    dstMacAddress = models.CharField(max_length=64, default='unverified')
    dstIpAddress = models.CharField(max_length=64, default='unverified')

class AppTerminationNotificationSubscription(models.Model):
    appInstanceId = models.CharField(max_length=64, default='unverified')
    subscriptionType = models.CharField(max_length=64, default='unverified')
    callbackReference = models.CharField(max_length=64, default='unverified')
    _links = models.CharField(max_length=64, default='unverified')
    self_referring_URI = models.CharField(max_length=64, default='unverified')