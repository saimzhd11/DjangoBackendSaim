# Generated by Django 4.0.3 on 2022-04-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HackademyAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attackinfo',
            name='AttackTitle',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='attackinfo',
            name='Attackdescription',
            field=models.CharField(max_length=400),
        ),
    ]