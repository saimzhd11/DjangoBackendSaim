# Generated by Django 4.0.5 on 2022-06-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttackInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AttackTitle', models.CharField(max_length=70)),
                ('AttackDescription', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ChallengesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryTitle', models.CharField(max_length=70)),
                ('CategoryDescription', models.TextField(default='')),
                ('Challenge1Description', models.TextField(default='')),
                ('Challenge2Description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='MachineCreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MachineName', models.CharField(max_length=70)),
                ('MachineType', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='MachinesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MachineNumber', models.IntegerField()),
                ('MachineName', models.CharField(max_length=70)),
                ('MachineType', models.CharField(max_length=70)),
                ('MachineLaunchDate', models.DateField()),
                ('MachineExpiryDate', models.DateField()),
                ('MachineTitle', models.CharField(default='defaultvalue', max_length=200)),
                ('MachineDescription', models.TextField()),
            ],
        ),
    ]
