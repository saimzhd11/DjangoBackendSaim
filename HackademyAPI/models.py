from django.db import models

# Create your models here.
class AttackInfo(models.Model):
    AttackTitle=models.CharField(max_length=70, blank=False)
    AttackDescription = models.TextField(default='',blank=False)

class MachinesInfo(models.Model):
    MachineNumber= models.IntegerField()
    MachineName= models.CharField(max_length=70, blank=False)
    MachineType= models.CharField(max_length=70, blank=False)
    MachineLaunchDate= models.DateField()
    MachineExpiryDate=models.DateField()
    MachineTitle= models.CharField(default="defaultvalue",max_length=200, blank=False)
    MachineDescription= models.TextField(blank=False)


class ChallengesInfo(models.Model):
    CategoryTitle=models.CharField(max_length=70, blank=False)
    CategoryDescription = models.TextField(default='',blank=False)
    Challenge1Description=models.TextField(default='',blank=False)
    Challenge2Description=models.TextField(default='',blank=False)

class MachineCreation(models.Model):
    MachineName=models.CharField(max_length=70, blank=False)
