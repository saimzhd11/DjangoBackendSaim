from django.urls import URLPattern, include, re_path
from HackademyAPI import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
   re_path(r'^attackinfo$',views.AttackInfoAPI),
   re_path(r'^attackinfo/([0-9]+)$',views.AttackInfoAPI),
   re_path(r'^userinfo$',views.UserInfoAPI),
   re_path(r'^userinfo/([0-9]+)$',views.UserInfoAPI),
   re_path(r'^machinesinfo$',views.MachinesInfoAPI),
   re_path(r'^machinesinfo/([0-9]+)$',views.MachinesInfoAPI),
   re_path(r'^challengesinfo$',views.ChallengesInfoAPI),
   re_path(r'^challengesinfo/([0-9]+)$',views.ChallengesInfoAPI),
    re_path(r'^machinecreation$',views.MachineCreationAPI),
   re_path(r'^machinecreation/([0-9]+)$',views.MachineCreationAPI),

]