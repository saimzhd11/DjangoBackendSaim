from rest_framework import serializers
from HackademyAPI.models import AttackInfo,MachinesInfo,ChallengesInfo,MachineCreation

class AttackInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=AttackInfo
        fields=('AttackTitle','AttackDescription')
class MachinesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=MachinesInfo
        fields=('MachineNumber','MachineName','MachineType','MachineLaunchDate','MachineExpiryDate','MachineDescription','MachineDescription')
class ChallengesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChallengesInfo
        fields=('CategoryTitle','CategoryDescription','Challenge1Description','Challenge2Description')
class MachineCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=MachineCreation
        fields=('MachineName','MachineType')