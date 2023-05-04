"""
URL configuration for freeMECPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Timing.views import *
from Applications.views import *
from Registrations.views import *

URI = {
    "allMecAppSupportSubscription": "mec_app_support/v2/applications/<str:appInstanceId>/subscriptions",
    "individualMecAppSupportSubscription": "mec_app_support/v2/applications/<str:appInstanceId>/subscriptions/<str:subscriptionId>",
    "allMecTrafficRule": "mec_app_support/v2/applications/<str:appInstanceId>/traffic_rules",
    "individualmecTrafficRule": "mec_app_support/v2/applications/<str:appInstanceId>/traffic_rules/<str:trafficRuleId>",
    "allMecDnsRule": "mec_app_support/v2/applications/<str:appInstanceId>/dns_rules",
    "individualMecDnsRule": "mec_app_support/v2/applications/<str:appInstanceId>/dns_rules/<str:dnsRuleId>",
    "confirmTerminationTask": "mec_app_support/v2/applications/<str:appInstanceId>/confirm_termination",
    "confirmReadyTask": "mec_app_support/v2/applications/<str:appInstanceId>/confirm_ready",
    "mecAppInstanceRegistration": "mec_app_support/v2/registrations",
    "mecTimingCaps": "mec_app_support/v2/timing/timing_caps",
    "mecCurrentTime": "mec_app_support/v2/timing/current_time"
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path(URI["allMecAppSupportSubscription"], allMecAppSupportSubscription),
    path(URI["individualMecAppSupportSubscription"], individualMecAppSupportSubscription),
    path(URI["allMecTrafficRule"], allMecTrafficRule),
    path(URI["individualmecTrafficRule"], individualmecTrafficRule),
    path(URI["allMecDnsRule"], allMecDnsRule),
    path(URI["individualMecDnsRule"], individualMecDnsRule),
    path(URI["confirmTerminationTask"], confirmTerminationTask),
    path(URI["confirmReadyTask"], confirmReadyTask),
    path(URI["mecAppInstanceRegistration"], mecAppInstanceRegistration),
    path(URI["mecTimingCaps"], mecTimingCaps),
    path(URI["mecCurrentTime"], mecCurrentTime),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
