from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Applications.models import *
from Registrations.models import *
from oauth2_provider.views.generic import ProtectedResourceView
import json
import uuid
import ast

class AllMecDnsRule(ProtectedResourceView):
    def get(self, request, appInstanceId):
        result = []
        status = 0
        if DnsRule.objects.filter(appInstanceId=appInstanceId).first():
            data = DnsRule.objects.filter(appInstanceId=appInstanceId)
            for i in range(len(data)):
                result.append({
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
        return JsonResponse(result, status=status, safe=False)

class AllMecAppSupportSubscription(ProtectedResourceView):
    def get(self, request, appInstanceId):
        result = {}
        status = 0
        return JsonResponse(result, status=status, safe=False)

    def post(self, request, appInstanceId):
        result = {}
        status = 0
        payload = json.loads(request.body.decode("utf-8"))
        if Subscription.objects.filter(appInstanceId=appInstanceId).first():
            pass
        result = {"SubscriptionLinkList": appInstanceId}
        return JsonResponse(result, status=status, safe=False)

class IndividualMecAppSupportSubscription(ProtectedResourceView):
    def get(self, request, appInstanceId, subscriptionId):
        pass

class AllMecTrafficRule(ProtectedResourceView):
    def get(self, request, appInstanceId):
        result = []
        status = 0
        if TrafficRule.objects.filter(appInstanceId=appInstanceId).first():
            data = TrafficRule.objects.filter(appInstanceId=appInstanceId)

            for i in range(len(data)):
                trafficFilter_UUID=data[i].trafficFilter_UUID
                dstInterface_UUID=data[i].dstInterface_UUID
                trafficFilter = TrafficFilter.objects.filter(trafficFilter_UUID=trafficFilter_UUID)
                dstInterface = DstInterface.objects.filter(dstInterface_UUID=dstInterface_UUID)

                trafficFilter_list = []
                dstInterface_list = []

                for tf in trafficFilter:
                    trafficFilter_list.append({
                        "srcAddress": ast.literal_eval(tf.srcAddress),
                        "dstAddress": ast.literal_eval(tf.dstAddress),
                        "srcPort": ast.literal_eval(tf.srcPort),
                        "dstPort": ast.literal_eval(tf.dstPort),
                        "protocol": ast.literal_eval(tf.protocol),
                        "token": ast.literal_eval(tf.token),
                        "srcTunnelAddress": ast.literal_eval(tf.srcTunnelAddress),
                        "tgtTunnelAddress": ast.literal_eval(tf.tgtTunnelAddress),
                        "srcTunnelPort": ast.literal_eval(tf.srcTunnelPort),
                        "dstTunnelPort": ast.literal_eval(tf.dstTunnelPort),
                        "qCI": tf.qCI,
                        "dSCP": tf.dSCP,
                        "tC": tf.tC
                    })

                for dif in dstInterface:
                    dstInterface_list.append({
                        "interfaceType": dif.interfaceType,
                        "tunnelInfo": {
                            "tunnelType": dif.tunnelType,
                            "tunnelDstAddress": dif.tunnelDstAddress,
                            "tunnelSrcAddress": dif.tunnelSrcAddress
                        },
                        "srcMacAddress": dif.srcMacAddress,
                        "dstMacAddress": dif.dstMacAddress,
                        "dstIpAddress": dif.dstIpAddress
                    })

                result.append({
                    "trafficRuleId": data[i].trafficRuleId,
                    "filterType": data[i].filterType,
                    "priority": data[i].priority,
                    "trafficFilter": trafficFilter_list,
                    "action": data[i].action,
                    "dstInterface": dstInterface_list,
                    "state": data[i].state,
                })
            status = 200
        else:
            result = {
                "status": 0,
                "message": "Dns rule does not exist."
            }
            status = 403
        return JsonResponse(result, status=status, safe=False)

class IndividualMecTrafficRule(ProtectedResourceView):
    def get(self, request, appInstanceId, trafficRuleId):
        result = {}
        status = 0
        if TrafficRule.objects.filter(trafficRuleId=trafficRuleId, appInstanceId=appInstanceId).first():
            data = TrafficRule.objects.get(trafficRuleId=trafficRuleId, appInstanceId=appInstanceId)
            
            trafficFilter_UUID=data.trafficFilter_UUID
            dstInterface_UUID=data.dstInterface_UUID
            trafficFilter = TrafficFilter.objects.filter(trafficFilter_UUID=trafficFilter_UUID)
            dstInterface = DstInterface.objects.filter(dstInterface_UUID=dstInterface_UUID)

            trafficFilter_list = []
            dstInterface_list = []

            for tf in trafficFilter:
                trafficFilter_list.append({
                    "srcAddress": ast.literal_eval(tf.srcAddress),
                    "dstAddress": ast.literal_eval(tf.dstAddress),
                    "srcPort": ast.literal_eval(tf.srcPort),
                    "dstPort": ast.literal_eval(tf.dstPort),
                    "protocol": ast.literal_eval(tf.protocol),
                    "token": ast.literal_eval(tf.token),
                    "srcTunnelAddress": ast.literal_eval(tf.srcTunnelAddress),
                    "tgtTunnelAddress": ast.literal_eval(tf.tgtTunnelAddress),
                    "srcTunnelPort": ast.literal_eval(tf.srcTunnelPort),
                    "dstTunnelPort": ast.literal_eval(tf.dstTunnelPort),
                    "qCI": tf.qCI,
                    "dSCP": tf.dSCP,
                    "tC": tf.tC
                })

            for dif in dstInterface:
                dstInterface_list.append({
                    "interfaceType": dif.interfaceType,
                    "tunnelInfo": {
                        "tunnelType": dif.tunnelType,
                        "tunnelDstAddress": dif.tunnelDstAddress,
                        "tunnelSrcAddress": dif.tunnelSrcAddress
                    },
                    "srcMacAddress": dif.srcMacAddress,
                    "dstMacAddress": dif.dstMacAddress,
                    "dstIpAddress": dif.dstIpAddress
                })

            result = {
                "trafficRuleId": data.trafficRuleId,
                "filterType": data.filterType,
                "priority": data.priority,
                "trafficFilter": trafficFilter_list,
                "action": data.action,
                "dstInterface": dstInterface_list,
                "state": data.state,
            }
            status = 200
        else:
            result = {
                "status": 0,
                "message": "Traffic rule does not exist."
            }
            status = 403
        return JsonResponse(result, status=status)

    def put(self, request, appInstanceId, trafficRuleId):
        payload = json.loads(request.body.decode("utf-8"))
        if TrafficRule.objects.filter(trafficRuleId=trafficRuleId, appInstanceId=appInstanceId).first():
            TrafficRule.objects.filter(trafficRuleId=trafficRuleId, appInstanceId=appInstanceId).update(
                filterType=payload["filterType"],
                priority=payload["priority"],
                action=payload["action"],
                state=payload["state"],
            )

            data = TrafficRule.objects.get(trafficRuleId=trafficRuleId, appInstanceId=appInstanceId)
            trafficFilter_UUID=data.trafficFilter_UUID
            dstInterface_UUID=data.dstInterface_UUID

            TrafficFilter.objects.filter(trafficFilter_UUID=trafficFilter_UUID).delete()
            for trafficFilter in payload["trafficFilter"]:
                TrafficFilter.objects.create(
                    trafficFilter_UUID=trafficFilter_UUID,
                    srcAddress=str(trafficFilter["srcAddress"]),
                    dstAddress=str(trafficFilter["dstAddress"]),
                    srcPort=str(trafficFilter["srcPort"]),
                    dstPort=str(trafficFilter["dstPort"]),
                    protocol=str(trafficFilter["protocol"]),
                    token=str(trafficFilter["token"]),
                    srcTunnelAddress=str(trafficFilter["srcTunnelAddress"]),
                    tgtTunnelAddress=str(trafficFilter["tgtTunnelAddress"]),
                    srcTunnelPort=str(trafficFilter["srcTunnelPort"]),
                    dstTunnelPort=str(trafficFilter["dstTunnelPort"]),
                    qCI=trafficFilter["srcAddress"],
                    dSCP=trafficFilter["dSCP"],
                    tC=trafficFilter["tC"]
                )
            
            DstInterface.objects.filter(dstInterface_UUID=dstInterface_UUID).delete()
            for dstInterface in payload["dstInterface"]:
                DstInterface.objects.create(
                    dstInterface_UUID=dstInterface_UUID,
                    interfaceType=dstInterface["interfaceType"],
                    tunnelType=dstInterface["tunnelInfo"]["tunnelType"],
                    tunnelDstAddress=dstInterface["tunnelInfo"]["tunnelDstAddress"],
                    tunnelSrcAddress=dstInterface["tunnelInfo"]["tunnelSrcAddress"],
                    srcMacAddress=dstInterface["srcMacAddress"],
                    dstMacAddress=dstInterface["dstMacAddress"],
                    dstIpAddress=dstInterface["dstIpAddress"]
                )

            data = TrafficRule.objects.get(trafficRuleId=trafficRuleId, appInstanceId=appInstanceId)
            
            trafficFilter_UUID=data.trafficFilter_UUID
            dstInterface_UUID=data.dstInterface_UUID
            trafficFilter = TrafficFilter.objects.filter(trafficFilter_UUID=trafficFilter_UUID)
            dstInterface = DstInterface.objects.filter(dstInterface_UUID=dstInterface_UUID)

            trafficFilter_list = []
            dstInterface_list = []

            for tf in trafficFilter:
                trafficFilter_list.append({
                    "srcAddress": ast.literal_eval(tf.srcAddress),
                    "dstAddress": ast.literal_eval(tf.dstAddress),
                    "srcPort": ast.literal_eval(tf.srcPort),
                    "dstPort": ast.literal_eval(tf.dstPort),
                    "protocol": ast.literal_eval(tf.protocol),
                    "token": ast.literal_eval(tf.token),
                    "srcTunnelAddress": ast.literal_eval(tf.srcTunnelAddress),
                    "tgtTunnelAddress": ast.literal_eval(tf.tgtTunnelAddress),
                    "srcTunnelPort": ast.literal_eval(tf.srcTunnelPort),
                    "dstTunnelPort": ast.literal_eval(tf.dstTunnelPort),
                    "qCI": tf.qCI,
                    "dSCP": tf.dSCP,
                    "tC": tf.tC
                })

            for dif in dstInterface:
                dstInterface_list.append({
                    "interfaceType": dif.interfaceType,
                    "tunnelInfo": {
                        "tunnelType": dif.tunnelType,
                        "tunnelDstAddress": dif.tunnelDstAddress,
                        "tunnelSrcAddress": dif.tunnelSrcAddress
                    },
                    "srcMacAddress": dif.srcMacAddress,
                    "dstMacAddress": dif.dstMacAddress,
                    "dstIpAddress": dif.dstIpAddress
                })

            result = {
                "trafficRuleId": data.trafficRuleId,
                "filterType": data.filterType,
                "priority": data.priority,
                "trafficFilter": trafficFilter_list,
                "action": data.action,
                "dstInterface": dstInterface_list,
                "state": data.state,
            }
            status = 200
        else:
            trafficFilter_UUID=str(uuid.uuid4())
            dstInterface_UUID=str(uuid.uuid4())

            TrafficRule.objects.create(
                appInstanceId=appInstanceId,
                trafficRuleId=payload["trafficRuleId"],
                filterType=payload["filterType"],
                priority=payload["priority"],
                trafficFilter_UUID=trafficFilter_UUID,
                action=payload["action"],
                dstInterface_UUID=dstInterface_UUID,
                state=payload["state"],
            )

            for trafficFilter in payload["trafficFilter"]:
                TrafficFilter.objects.create(
                    trafficFilter_UUID=trafficFilter_UUID,
                    srcAddress=str(trafficFilter["srcAddress"]),
                    dstAddress=str(trafficFilter["dstAddress"]),
                    srcPort=str(trafficFilter["srcPort"]),
                    dstPort=str(trafficFilter["dstPort"]),
                    protocol=str(trafficFilter["protocol"]),
                    token=str(trafficFilter["token"]),
                    srcTunnelAddress=str(trafficFilter["srcTunnelAddress"]),
                    tgtTunnelAddress=str(trafficFilter["tgtTunnelAddress"]),
                    srcTunnelPort=str(trafficFilter["srcTunnelPort"]),
                    dstTunnelPort=str(trafficFilter["dstTunnelPort"]),
                    qCI=trafficFilter["srcAddress"],
                    dSCP=trafficFilter["dSCP"],
                    tC=trafficFilter["tC"]
                )

            for dstInterface in payload["dstInterface"]:
                DstInterface.objects.create(
                    dstInterface_UUID=dstInterface_UUID,
                    interfaceType=dstInterface["interfaceType"],
                    tunnelType=dstInterface["tunnelInfo"]["tunnelType"],
                    tunnelDstAddress=dstInterface["tunnelInfo"]["tunnelDstAddress"],
                    tunnelSrcAddress=dstInterface["tunnelInfo"]["tunnelSrcAddress"],
                    srcMacAddress=dstInterface["srcMacAddress"],
                    dstMacAddress=dstInterface["dstMacAddress"],
                    dstIpAddress=dstInterface["dstIpAddress"]
                )

            data = TrafficRule.objects.get(trafficRuleId=trafficRuleId, appInstanceId=appInstanceId)
            
            trafficFilter_UUID=data.trafficFilter_UUID
            dstInterface_UUID=data.dstInterface_UUID
            trafficFilter = TrafficFilter.objects.filter(trafficFilter_UUID=trafficFilter_UUID)
            dstInterface = DstInterface.objects.filter(dstInterface_UUID=dstInterface_UUID)

            trafficFilter_list = []
            dstInterface_list = []

            for tf in trafficFilter:
                trafficFilter_list.append({
                    "srcAddress": ast.literal_eval(tf.srcAddress),
                    "dstAddress": ast.literal_eval(tf.dstAddress),
                    "srcPort": ast.literal_eval(tf.srcPort),
                    "dstPort": ast.literal_eval(tf.dstPort),
                    "protocol": ast.literal_eval(tf.protocol),
                    "token": ast.literal_eval(tf.token),
                    "srcTunnelAddress": ast.literal_eval(tf.srcTunnelAddress),
                    "tgtTunnelAddress": ast.literal_eval(tf.tgtTunnelAddress),
                    "srcTunnelPort": ast.literal_eval(tf.srcTunnelPort),
                    "dstTunnelPort": ast.literal_eval(tf.dstTunnelPort),
                    "qCI": tf.qCI,
                    "dSCP": tf.dSCP,
                    "tC": tf.tC
                })

            for dif in dstInterface:
                dstInterface_list.append({
                    "interfaceType": dif.interfaceType,
                    "tunnelInfo": {
                        "tunnelType": dif.tunnelType,
                        "tunnelDstAddress": dif.tunnelDstAddress,
                        "tunnelSrcAddress": dif.tunnelSrcAddress
                    },
                    "srcMacAddress": dif.srcMacAddress,
                    "dstMacAddress": dif.dstMacAddress,
                    "dstIpAddress": dif.dstIpAddress
                })

            result = {
                "trafficRuleId": data.trafficRuleId,
                "filterType": data.filterType,
                "priority": data.priority,
                "trafficFilter": trafficFilter_list,
                "action": data.action,
                "dstInterface": dstInterface_list,
                "state": data.state,
            }
            status = 200
        return JsonResponse(result, status=status)

class IndividualMecDnsRule(ProtectedResourceView):
    def get(self, request, appInstanceId, dnsRuleId):
        result = {}
        status = 0
        if DnsRule.objects.filter(dnsRuleId=dnsRuleId).first():
            data = DnsRule.objects.get(dnsRuleId=dnsRuleId)
            result = {
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
        return JsonResponse(result, status=status)

    def put(self, request, appInstanceId, dnsRuleId):
        payload = json.loads(request.body.decode("utf-8"))
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
                "dnsRuleId": data.dnsRuleId,
                "domainName": data.domainName,
                "ipAddressType": data.ipAddressType,
                "ipAddress": data.ipAddress,
                "ttl": data.ttl,
                "state": data.state,
            }
            status = 200
        return JsonResponse(result, status=status)

class ConfirmTerminationTask(ProtectedResourceView):
    def get(self, request, appInstanceId):
        result = {}
        status = 0
        return JsonResponse(result, status=status)

class ConfirmReadyTask(ProtectedResourceView):
    def get(self, request, appInstanceId):
        result = {}
        status = 0
        return JsonResponse(result, status=status)