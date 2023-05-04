from django.shortcuts import render
from django.http import JsonResponse
from .forms import RegisterForm
from .models import MecApp, AppInfo
from django.contrib import auth as Auth
import json
# Create your views here.
# def login(request):
#     if request.method != "POST":
#         return JsonResponse({
#             "status": 1,
#             "message": "error"
#             })
#     name = request.POST['name']
#     password = request.POST['password']
#     if name == "admin": # 預設管理者
#         password = "admin"
#         register(request)
#     user = Auth.authenticate(username=name, password=password)

#     if not user:
#         return JsonResponse({
#             "status": 1,
#             "message": "無此帳號"
#             })
#     else:
#         Auth.login(request, user)
#         uu_id = user.id
#         role = user.role
#         if role not in ["tenant", "admin"]:
#             rep = JsonResponse({
#             "status": 1,
#             "message": "該帳號未被授權"
#             })
#         else:
#             payload = {
#                 "name": name,
#                 "exp": datetime.utcnow() + timedelta(minutes=10)
#             }
#             token = jwt.encode(payload, "mnmn5g", algorithm='HS256').decode('utf-8')
#             rep = JsonResponse({
#                 "status": 0,
#                 "message": "登入成功",
#                 "role": role
#                 })
#             rep.set_cookie('token', token)
#             rep.set_cookie('uu_id', uu_id)
#         return rep


# def register(appInstanceId):
#     if request.method == 'POST':
#         # print(request.POST)
#         # data = request.body.decode("utf-8")
#         # input(data)
#         # data = json.loads(data)
#         f = RegisterForm(["appInstanceId":appInstanceId])
#         if f.is_valid():
#             name = appInstanceId
#             # password = f.cleaned_data['password']

#             if name == "admin": # 預設管理者
#                 password == "admin"
#                 if not MecApp.objects.filter(username=name).first():
#                     user_db = MecApp(
#                         username=name,
#                         role="admin",
#                         is_superuser=True,
#                         is_staff=True
#                     )
#                     user_db.set_password(password)
#                     user_db.save()
#                     return JsonResponse({
#                         "status": 0,
#                         "message": "註冊成功"
#                         })

#             else:
#                 if MecApp.objects.filter(username=name).first():
#                     return JsonResponse({
#                         "status": 1,
#                         "message": "使用者名稱重複"
#                     })
#                 user_db = MecApp(
#                     username=name,
#                     role="unverified"
#                 )

#                 user_db.set_password(password)
#                 user_db.save()
#                 return JsonResponse({
#                     "status": 0,
#                     "message": "註冊成功"
#                     })

#     return {
#             "status": 1,
#             "message": "no get"
#             }


def mecAppInstanceRegistration(request):
    if request.method == "POST":
        appName = request.POST["appName"]
        appProvider = request.POST["appProvider"]
        appCategory = request.POST["appCategory"]
        appDId = request.POST["appDId"]
        appInstanceId = request.POST["appInstanceId"]
        endpoint = request.POST["endpoint"]
        appServiceRequired = request.POST["appServiceRequired"]
        appServiceOptional = request.POST["appServiceOptional"]
        appFeatureRequired = request.POST["appFeatureRequired"]
        appFeatureOptional = request.POST["appFeatureOptional"]
        isInsByMec = request.POST["isInsByMec"]
        appProfile = request.POST["appProfile"]

        if AppInfo.objects.filter(appInstanceId=appInstanceId).first():
            result = {
                "status": 1,
                "message": "The mec app is registrated"
            }
            return JsonResponse(result, status=403)


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

        result = {
            "status": 0
        }

        return JsonResponse(result, status=201)
    else:
        result = {
            "status": 1,
            "message": "method error"
        }
        JsonResponse(result, status=404)