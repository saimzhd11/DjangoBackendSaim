# Generated by Django 4.0.5 on 2022-06-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HackademyAPI', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=70)),
                ('LastName', models.CharField(max_length=70)),
                ('HomeAddress', models.TextField(default='')),
                ('City', models.CharField(max_length=70)),
                ('Country', models.CharField(max_length=70)),
                ('PostalCode', models.IntegerField()),
                ('UserDescription', models.TextField(default='')),
            ],
        ),
    ]
