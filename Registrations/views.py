from django.shortcuts import render
from django.http import JsonResponse
from .forms import RegisterForm
from .models import MecApp, AppInfo
from django.contrib import auth as Auth
from utils.client_credential import *
from django.contrib.sessions.backends.db import SessionStore
import json
from django.views.decorators.csrf import csrf_exempt
from freeMECPlatform.settings import CLIENT_ID, SECRET

@csrf_exempt
def mecAppInstanceRegistration(request):
    if request.method == "POST":
        payload = json.loads(request.body.decode("utf-8"))

        appName = payload["appName"]
        appProvider = payload["appProvider"]
        appCategory = payload["appCategory"]
        appDId = payload["appDId"]
        appInstanceId = payload["appInstanceId"]
        endpoint = payload["endpoint"]
        appServiceRequired = payload["appServiceRequired"]
        appServiceOptional = payload["appServiceOptional"]
        appFeatureRequired = payload["appFeatureRequired"]
        appFeatureOptional = payload["appFeatureOptional"]
        isInsByMec = payload["isInsByMec"]
        appProfile = payload["appProfile"]



        credential = gen_client_credential(CLIENT_ID, SECRET)
        token = gen_token(credential)

        AppInfo.objects.create(
            appName=appName,
            appProvider=appProvider,
            appCategory=appCategory,
            appDId=appDId,
            appInstanceId=appInstanceId,
            endpoint=endpoint,
            appServiceRequired=appServiceRequired,
            appServiceOptional=appServiceOptional,
            appFeatureRequired=appFeatureRequired,
            appFeatureOptional=appFeatureOptional,
            isInsByMec=isInsByMec,
            appProfile=appProfile,
        )

        payload["token"] = token
        result = payload

        return JsonResponse(result, status=201)
    else:
        result = {
            "status": 1,
            "message": "method error"
        }
        JsonResponse(result, status=404)