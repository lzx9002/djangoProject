import platform
import json
import django
import psutil
from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from api.models import User_name_list
from cpuUsage import histories


# Create your views here.


@csrf_exempt
# 接收请求数据
def login_api(request):
    if request.POST:
        name = request.POST['username']
        password = request.POST['password']
        rows = User_name_list.objects.filter(username=name)
        if rows and rows[0].password == password:
            return JsonResponse({
                "code": 0,
                "msg": "登录成功",
                "data": {
                    "username": name,
                    "access_token": name,
                }
            })

        return JsonResponse({
            "ode": -1,
            "msg": "用户名或密码错误"
        })


@csrf_exempt
def userinfo(request):
    if request.method == 'POST':
        try:
            token = request.POST['token']
        except KeyError:
            pass
        else:
            rows = User_name_list.objects.filter(username=token)
            if rows:
                return JsonResponse({
                    "code": 0,
                    "msg": "",
                    "data": {"role": rows[0].role.id,
                             "username": token,
                             "user": rows[0].nickname,
                             "sex": rows[0].sex,

                             }
                })
            return JsonResponse({
                "code": 401,
                "msg": '未登录',
                "data": {}
            })
        return JsonResponse({
            "code": 401,
            "msg": '未登录',
            "data": {}
        })


def systeminfo(request):
    if request.method == 'POST':
        return JsonResponse({
            "code": 0,
            "msg": "",
            "data": {
                "platform": platform.system(),
                "version": platform.version(),
                "release": platform.release(),
                "name": platform.node(),
                "cpu_count": psutil.cpu_count(),
                "TotalMemory": int(Decimal(psutil.virtual_memory().total / 1024 / 1024 / 1024).quantize(Decimal("0.01"),
                                                                                                        rounding="ROUND_HALF_UP")),
                "MemoryUsageRate": int(
                    Decimal(psutil.virtual_memory().used / 1024 / 1024 / 1024).quantize(Decimal("0.01"),
                                                                                        rounding="ROUND_HALF_UP")),
                "processor": platform.processor(),
                "pythonVersion": platform.python_version(),
                "djangoVersion": django.__version__,
            }
        })


def cpuMemoryInfo(request):
    if request.method == 'POST':
        interval: float = 0.5
        return JsonResponse({
            "code": 0,
            "msg": "",
            "data": {
                "cpu": psutil.cpu_percent(interval=interval),
                "cpu_count": psutil.cpu_percent(interval=interval, percpu=True),
                "memory": psutil.virtual_memory().percent,
                "TotalMemory": Decimal(psutil.virtual_memory().total / 1024 / 1024 / 1024).quantize(Decimal("0.01"),
                                                                                                    rounding="ROUND_HALF_UP"),
                "MemoryUsageRate": Decimal(psutil.virtual_memory().used / 1024 / 1024 / 1024).quantize(Decimal("0.01"),
                                                                                                       rounding="ROUND_HALF_UP"),
            }
        })


def CPUUsageOverview(request):
    if request.method == 'POST':
        return JsonResponse({
            "code": 0,
            "msg": "",
            "data": histories
        })
