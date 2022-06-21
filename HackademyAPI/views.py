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
import os
import itertools
import threading
import time
import sys
import xml.etree.ElementTree as ET
# from termcolor import colored
# Create your views here.
@csrf_exempt
def AttackInfoAPI(request,id=0):
    if request.method=='GET':   
        attackinfo = AttackInfo.objects.all()
        attackinfo_serializer=AttackInfoSerializer(attackinfo,many=True)
        return JsonResponse(attackinfo_serializer.data,safe=False)
    elif request.method=='POST':    
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
    



ET.register_namespace("","http://www.github/cliffe/SecGen/scenario")
ET.register_namespace("","http://www.w3.org/2001/XMLSchema-instance")
ET.register_namespace("","http://www.github/cliffe/SecGen/scenario")
pathM = 'sudo ruby secgen.rb -s scenarios/examples/vulnerability_examples/'
newfile = ("Updated.xml")
tree = ET.parse('HackademyAPI/dirtycow.xml')
root = tree.getroot()


@csrf_exempt
def MachineCreationAPI(request, id=3):
    if request.method=='POST': 
        if 'MachineName' in request.POST:
            MachineName = request.POST['MachineName']
        if 'MachineType' in request.POST:
            MachineType = request.POST['MachineType']
        if 'CreationDate' in request.POST:
            CreationDate = request.POST['CreationDate']
        if 'ExpiryDate' in request.POST:
            ExpiryDate = request.POST['ExpiryDate']
        if 'MachineDescription' in request.POST:
            MachineDescription = request.POST['MachineDescription']
        if 'Vulnerability' in request.POST:
            Vulnerability = request.POST['Vulnerability']
        if 'Difficulty' in request.POST:
            Difficulty = request.POST['Difficulty']
        if 'Encoders' in request.POST:
            Encoders = request.POST['Encoders']
        if 'Network' in request.POST:
            Network = request.POST['Network']
        if 'Service' in request.POST:
            Service = request.POST['Service']
        if 'webapp' in request.POST:
            webapp = request.POST['webapp']
        if 'generator' in request.POST:
            generator = request.POST['generator']
        if 'Service' in request.POST:
            datastore = request.POST['datastore']
      

    print("Hello world",MachineName, MachineType,CreationDate,ExpiryDate,MachineDescription,Vulnerability,Difficulty,Encoders,Network,Service,webapp,generator,datastore)
         
    
    for x in root.findall(".//{http://www.github/cliffe/SecGen/scenario}vulnerability"):
        x.attrib['module_path']=f'{Vulnerability}'
        print(x.attrib)
    

    for x in root.findall(".//{http://www.github/cliffe/SecGen/scenario}difficulty"):
        x.text = f'{Difficulty}'
        print(x.text)
    

    for x in tree.findall(".//{http://www.github/cliffe/SecGen/scenario}encoder"):
        x.attrib['name'] = f'{Encoders}'
        print(x.attrib)
    

    for x in tree.findall(".//{http://www.github/cliffe/SecGen/scenario}network"):
        x.attrib['type'] = f'{Network}'  
        print(x.attrib)
    

    for x in root.findall(".//{http://www.github/cliffe/SecGen/scenario}type"):
        x.text = f'{MachineType}'
        print(x.text)
    
    tree.write(newfile)

    os.chdir("/home/wasi/SecGen")
    time.sleep(2)
    # os.chdir("/SecGen")
    # time.sleep(2)
    os.system(pathM+"dirtycow.xml run") 


    return HttpResponse("Not POST")

    if __name__ == '__main__':
        app.run(host="192.168.252.128")