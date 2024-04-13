from django.db import models


# Create your models here.
class User_role_list(models.Model):
    role_name = models.CharField(max_length=100)
    limits = models.CharField(max_length=100)
    descr = models.CharField(max_length=100)
    checks = models.CharField(max_length=5)


class User_name_list(models.Model):
    username = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=128, null=False)
    nickname = models.CharField(max_length=150, null=False, blank=False)
    sex = models.CharField(max_length=50, null=False, blank=False)
    avatar = models.URLField(max_length=100, null=True, blank=True)
    cellphone = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    remarks = models.TextField(max_length=500, null=True, blank=True)
    role = models.OneToOneField(User_role_list, on_delete=models.CASCADE)

