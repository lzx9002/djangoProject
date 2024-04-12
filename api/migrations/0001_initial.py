# Generated by Django 5.0.3 on 2024-04-11 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='System_usage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('cpu', models.FloatField(blank=True, null=True)),
                ('memory', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_role_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('limits', models.CharField(max_length=100)),
                ('descr', models.CharField(max_length=100)),
                ('checks', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User_name_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
                ('nickname', models.CharField(max_length=150)),
                ('sex', models.CharField(max_length=50)),
                ('avatar', models.URLField(blank=True, max_length=100, null=True)),
                ('cellphone', models.BigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('remarks', models.TextField(blank=True, max_length=500, null=True)),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.user_role_list')),
            ],
        ),
    ]
