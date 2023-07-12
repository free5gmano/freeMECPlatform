from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
from django.views.decorators.csrf import csrf_exempt
from utils.client_credential import *
from freeMECPlatform.settings import CLIENT_ID, SECRET

# Create your views here

@csrf_exempt
def service_registration(request, appInstanceId):
    if request.method == "POST":
        credential = gen_client_credential(CLIENT_ID, SECRET)
        token = gen_token(credential)
        result = {
            "serInstanceId": appInstanceId.split("--")[0],
            "serName": "AMS",
            "serCategory": {
                "href": appInstanceId.split("--")[1],
                "id": "string",
                "name": "string",
                "version": "string"
            },
            "version": "string",
            "state": "ACTIVE",
            "transportInfo": {
                "id": appInstanceId.split("--")[0],
                "name": "AMS",
                "description": "string",
                "type": "REST_HTTP",
                "protocol": "HTTP",
                "version": "1.0",
                "security": {
                "oAuth2Info": {
                    "grantTypes": [
                    "OAUTH2_AUTHORIZATION_CODE"
                    ],
                    "tokenEndpoint": token
                }
                },
                "implSpecificInfo": {}
            },
            "serializer": "JSON",
            "scopeOfLocality": "MEC_SYSTEM",
            "consumedLocalOnly": True,
            "isLocal": True,
            "livenessInterval": 0,
            "_links": {
                "self": {
                "href": "string"
                },
                "liveness": {
                "href": "string"
                }
            }
        }
        status = 201
        return JsonResponse(result, status=status, safe=False)
    elif request.method == "GET":
        result = {
            "serInstanceId": appInstanceId.split("--")[0],
            "serName": "AMS",
            "serCategory": {
                "href": "10.0.0.218:34567",
                "id": "string",
                "name": "RNIS",
                "version": "string"
            },
            "version": "string",
            "state": "ACTIVE",
            "transportInfo": {
                "id": appInstanceId.split("--")[0],
                "name": "AMS",
                "description": "string",
                "type": "REST_HTTP",
                "protocol": "HTTP",
                "version": "1.0",
                "security": {
                "oAuth2Info": {
                    "grantTypes": [
                    "OAUTH2_AUTHORIZATION_CODE"
                    ],
                    "tokenEndpoint": "token"
                }
                },
                "implSpecificInfo": {}
            },
            "serializer": "JSON",
            "scopeOfLocality": "MEC_SYSTEM",
            "consumedLocalOnly": True,
            "isLocal": True,
            "livenessInterval": 0,
            "_links": {
                "self": {
                "href": "string"
                },
                "liveness": {
                "href": "string"
                }
            }
        }
        status = 201
        return JsonResponse(result, status=status, safe=False)

@csrf_exempt
def service_query(request, appInstanceId, serviceId):
    if request.method == "POST":
        credential = gen_client_credential(CLIENT_ID, SECRET)
        token = gen_token(credential)
        result = {
            "serInstanceId": "string",
            "serName": "string",
            "serCategory": {
                "href": "10.0.0.218:4567",
                "id": "string",
                "name": "string",
                "version": "string"
            },
            "version": "string",
            "state": "ACTIVE",
            "transportInfo": {
                "id": "string",
                "name": "string",
                "description": "string",
                "type": "REST_HTTP",
                "protocol": "string",
                "version": "string",
                "security": {
                "oAuth2Info": {
                    "grantTypes": [
                    "OAUTH2_AUTHORIZATION_CODE"
                    ],
                    "tokenEndpoint": "string"
                }
                },
                "implSpecificInfo": {}
            },
            "serializer": "JSON",
            "scopeOfLocality": "MEC_SYSTEM",
            "consumedLocalOnly": True,
            "isLocal": True,
            "livenessInterval": 0,
            "_links": {
                "self": {
                "href": "string"
                },
                "liveness": {
                "href": "string"
                }
            }
        }
        status = 201
        return JsonResponse(result, status=status, safe=False)


class AlllService(ProtectedResourceView):
    def get(request, appInstanceId):
        result = []
        status = 0

        return JsonResponse(result, status=status)

    def post(request, appInstanceId):
        result = []
        status = 0

        return JsonResponse(result, status=status)

class AlllService(ProtectedResourceView):
    def get(request, appInstanceId):
        result = []
        status = 0

        return JsonResponse(result, status=status)

    def post(request, appInstanceId):
        result = []
        status = 0

        return JsonResponse(result, status=status)