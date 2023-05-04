from django.shortcuts import render
from django.http import JsonResponse
from .utils.putPayloadParser import put_payload_parser
from Applications.models import *
from Registrations.models import *

# Create your views here.

def allMecAppSupportSubscription(request, appInstanceId):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        result = {"SubscriptionLinkList": appInstanceId}
        return JsonResponse(result, status=201)

def individualMecAppSupportSubscription(request, appInstanceId, subscriptionId):
    pass

def allMecTrafficRule(request, appInstanceId):
    result = {"TrafficRulesArray":[]}
    status = 0
    if request.method == "GET":
        if TrafficRule.objects.filter(appInstanceId=appInstanceId).first():
            data = TrafficRule.objects.filter(appInstanceId=appInstanceId)
            for i in range(len(data)):
                result["TrafficRulesArray"].append({
                    "trafficRuleId": data[i].trafficRuleId,
                    "filterType": data[i].filterType,
                    "priority": data[i].priority,
                    "trafficFilter": data[i].trafficFilter,
                    "action": data[i].action,
                    "dstInterface": data[i].dstInterface,
                    "state": data[i].state,
                })
            status = 200
        else:
            result = {
                "status": 0,
                "message": "Dns rule does not exist."
            }
            status = 403
    else:
        result = {
            "status": 1,
            "message": "method error"
        }
    return JsonResponse(result, status=404)

def individualmecTrafficRule(request, appInstanceId, trafficRuleId):
    result = {}
    status = 0
    if request.method == "GET":
        if TrafficRule.objects.filter(trafficRuleId=trafficRuleId).first():
            data = TrafficRule.objects.get(trafficRuleId=trafficRuleId)
            result = {
                "appInstanceId": data.appInstanceId,
                "trafficRuleId": data.trafficRuleId,
                "filterType": data.filterType,
                "priority": data.priority,
                "trafficFilter": data.trafficFilter,
                "action": data.action,
                "dstInterface": data.dstInterface,
                "state": data.state,
            }
            status = 200
        else:
            result = {
                "status": 0,
                "message": "Traffic rule does not exist."
            }
            status = 403
    elif request.method == "PUT":
        payload = put_payload_parser(request)
        if TrafficRule.objects.filter(trafficRuleId=trafficRuleId).first():
            TrafficRule.objects.filter(trafficRuleId=trafficRuleId).update(
                trafficRuleId=payload["trafficRuleId"],
                filterType=payload["filterType"],
                priority=payload["priority"],
                trafficFilter=payload["trafficFilter"],
                action=payload["action"],
                dstInterface=payload["dstInterface"],
                state=payload["state"],
            )
            data = TrafficRule.objects.get(trafficRuleId=trafficRuleId)
            result = {
                "appInstanceId": data.appInstanceId,
                "trafficRuleId": data.trafficRuleId,
                "filterType": data.filterType,
                "priority": data.priority,
                "trafficFilter": data.trafficFilter,
                "action": data.action,
                "dstInterface": data.dstInterface,
                "state": data.state,
            }
            status = 200
        else:
            TrafficRule.objects.create(
                appInstanceId=appInstanceId,
                trafficRuleId=payload["trafficRuleId"],
                filterType=payload["filterType"],
                priority=payload["priority"],
                trafficFilter=payload["trafficFilter"],
                action=payload["action"],
                dstInterface=payload["dstInterface"],
                state=payload["state"],
            )
            data = TrafficRule.objects.get(trafficRuleId=trafficRuleId)
            result = {
                "appInstanceId": data.appInstanceId,
                "trafficRuleId": data.trafficRuleId,
                "filterType": data.filterType,
                "priority": data.priority,
                "trafficFilter": data.trafficFilter,
                "action": data.action,
                "dstInterface": data.dstInterface,
                "state": data.state,
            }
            status = 200
    else:
        result = {
            "status": 1,
            "message": "method error"
        }
        status = 404
    return JsonResponse(result, status=status)
    
def allMecDnsRule(request, appInstanceId):
    result = {"TrafficRulesArray":[]}
    status = 0
    if request.method == "GET":
        if DnsRule.objects.filter(appInstanceId=appInstanceId).first():
            data = DnsRule.objects.filter(appInstanceId=appInstanceId)
            for i in range(len(data)):
                result["TrafficRulesArray"].append({
                    "dnsRuleId":data[i].dnsRuleId,
                    "domainName": data[i].domainName,
                    "ipAddressType": data[i].ipAddressType,
                    "ipAddress": data[i].ipAddress,
                    "ttl": data[i].ttl,
                    "state": data[i].state,
                })
            status = 200
        else:
            result = {
                "status": 0,
                "message": "Dns rule does not exist."
            }
            status = 403
    else:
        result = {
            "status": 1,
            "message": "method error"
        }
    return JsonResponse(result, status=404)

def individualMecDnsRule(request, appInstanceId, dnsRuleId):
    result = {}
    status = 0
    if request.method == "GET":
        if DnsRule.objects.filter(dnsRuleId=dnsRuleId).first():
            data = DnsRule.objects.get(dnsRuleId=dnsRuleId)
            result = {
                "appInstanceId": data.appInstanceId,
                "dnsRuleId": data.dnsRuleId,
                "domainName": data.domainName,
                "ipAddressType": data.ipAddressType,
                "ipAddress": data.ipAddress,
                "ttl": data.ttl,
                "state": data.state,
            }
            status = 200
        else:
            result = {
                "status": 0,
                "message": "Dns rule does not exist."
            }
            status = 403
    elif request.method == "PUT":
        payload = put_payload_parser(request)
        if DnsRule.objects.filter(dnsRuleId=dnsRuleId).first():
            DnsRule.objects.filter(dnsRuleId=dnsRuleId).update(
                dnsRuleId=payload["dnsRuleId"],
                domainName=payload["domainName"],
                ipAddressType=payload["ipAddressType"],
                ipAddress=payload["ipAddress"],
                ttl=payload["ttl"],
                state=payload["state"],
            )
            data = DnsRule.objects.get(dnsRuleId=dnsRuleId)
            result = {
                "appInstanceId": data.appInstanceId,
                "dnsRuleId": data.dnsRuleId,
                "domainName": data.domainName,
                "ipAddressType": data.ipAddressType,
                "ipAddress": data.ipAddress,
                "ttl": data.ttl,
                "state": data.state,
            }
            status = 200
        else:
            DnsRule.objects.create(
                appInstanceId=appInstanceId,
                dnsRuleId=payload["dnsRuleId"],
                domainName=payload["domainName"],
                ipAddressType=payload["ipAddressType"],
                ipAddress=payload["ipAddress"],
                ttl=payload["ttl"],
                state=payload["state"],
            )
            data = DnsRule.objects.get(dnsRuleId=dnsRuleId)
            result = {
                "appInstanceId": data.appInstanceId,
                "dnsRuleId": data.dnsRuleId,
                "domainName": data.domainName,
                "ipAddressType": data.ipAddressType,
                "ipAddress": data.ipAddress,
                "ttl": data.ttl,
                "state": data.state,
            }
            status = 200
    else:
        result = {
            "status": 1,
            "message": "method error"
        }
        status = 404
    return JsonResponse(result, status=status)

def confirmTerminationTask(request, appInstanceId):
    pass

def confirmReadyTask(request, appInstanceId):
    pass