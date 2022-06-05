from cgi import print_arguments
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from HackademyAPI.models import AttackInfo,MachinesInfo,ChallengesInfo,MachineCreation
from HackademyAPI.Serializers import AttackInfoSerializer,MachinesInfoSerializer,ChallengesInfoSerializer,MachineCreationSerializer
from django.core.files.storage import default_storage
from rest_framework import viewsets
# Create your views here.
@csrf_exempt
def AttackInfoAPI(request,id=0):
    if request.method=='GET':   
        attackinfo = AttackInfo.objects.all()
        attackinfo_serializer=AttackInfoSerializer(attackinfo,many=True)
        return JsonResponse(attackinfo_serializer.data,safe=False)
    elif request.method=='POST':    
        # if 'AttackTitle' in request.POST:
        #     AttackTitle = request.POST['AttackTitle']
        #     print("Yo whatup",AttackTitle)
        #     return HttpResponse('success') # if everything is OK
        # return HttpResponse("Unsucccesss0")
        attackinfo_data=JSONParser().parse(request)
        attackinfo_serializer=AttackInfoSerializer(data=attackinfo_data)
        if attackinfo_serializer.is_valid():
            attackinfo_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
        

@csrf_exempt
def MachinesInfoAPI(request,id=1):
    if request.method=='GET':
        machinesinfo = MachinesInfo.objects.all()
        machinesinfo_serializer=MachinesInfoSerializer(machinesinfo,many=True)
        return JsonResponse(machinesinfo_serializer.data,safe=False)
    elif request.method=='POST':
        machinesinfo_data=JSONParser().parse(request)
        machinesinfo_serializer=MachinesInfoSerializer(data=machinesinfo_data)
        if machinesinfo_serializer.is_valid():
            machinesinfo_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

@csrf_exempt
def ChallengesInfoAPI(request,id=2):
    if request.method=='GET':   
        challengesinfo = ChallengesInfo.objects.all()
        challengesinfo_serializer=ChallengesInfoSerializer(challengesinfo,many=True)
        return JsonResponse(challengesinfo_serializer.data,safe=False)
    elif request.method=='POST':
        challengesinfo_data=JSONParser().parse(request)
        challengesinfo_serializer=ChallengesInfoSerializer(data=challengesinfo_data)
        if challengesinfo_serializer.is_valid():
            challengesinfo_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    
@csrf_exempt
def MachineCreationAPI(request, id=3):
    if request.method=='POST': 
        if 'MachineName' in request.POST:
                MachineName = request.POST['MachineName']
                # print("Yo whatup",MachineName)
                return HttpResponse('success') # if everything is OK
        return HttpResponse("Unsucccesss0")