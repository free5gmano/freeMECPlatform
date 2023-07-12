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
from MECServiceManagement.views import *

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
    "mecCurrentTime": "mec_app_support/v2/timing/current_time",
    # "serviceAvailabilityQuery": "mec_service_mgmt/v1/applications/<str:appInstanceId>/services",
    "serviceRegistration": "mec_service_mgmt/v1/applications/<str:appInstanceId>/services",
    "individualServiceAvailabilityQuery": "mec_service_mgmt/v1/applications/<str:appInstanceId>/services/<str:serviceId>",
    # "individualServiceUpdates": "mec_service_mgmt/v1/applications/<str:appInstanceId>/services/<str:serviceId>",
    # "individualServiceDelete": "mec_service_mgmt/v1/applications/<str:appInstanceId>/services/<str:serviceId>"
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path(URI["allMecAppSupportSubscription"], AllMecAppSupportSubscription.as_view()),
    path(URI["individualMecAppSupportSubscription"], IndividualMecAppSupportSubscription.as_view()),
    path(URI["allMecTrafficRule"], AllMecTrafficRule.as_view()),
    path(URI["individualmecTrafficRule"], IndividualMecTrafficRule.as_view()),
    path(URI["allMecDnsRule"], AllMecDnsRule.as_view()),
    path(URI["individualMecDnsRule"], IndividualMecDnsRule.as_view()),
    path(URI["confirmTerminationTask"], ConfirmTerminationTask.as_view()),
    path(URI["confirmReadyTask"], ConfirmReadyTask.as_view()),
    path(URI["mecAppInstanceRegistration"], mecAppInstanceRegistration),
    path(URI["mecTimingCaps"], mecTimingCaps),
    path(URI["mecCurrentTime"], mecCurrentTime),
    # path(URI["serviceAvailabilityQuery"], mecCurrentTime),
    path(URI["serviceRegistration"], service_registration),
    path(URI["individualServiceAvailabilityQuery"], service_query),
    # path(URI["individualServiceUpdates"], mecCurrentTime),
    # path(URI["individualServiceDelete"], mecCurrentTime),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
