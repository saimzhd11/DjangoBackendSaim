# Generated by Django 4.0.3 on 2022-05-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HackademyAPI', '0004_challengesinfo_alter_attackinfo_attackdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinesinfo',
            name='MachineTitle',
            field=models.CharField(default='defaultvalue', max_length=200),
        ),
    ]