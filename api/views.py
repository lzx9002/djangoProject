import platform
from decimal import Decimal

import django
import psutil

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import User_name_list


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
        token = request.POST['token']
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


def logout_api(request):
    if request.method == 'POST':
        response = HttpResponse('{"code": 0}')
        response.delete_cookie('password')
        response.delete_cookie('username')
        return response

    return HttpResponse("")


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
                "TotalMemory": Decimal(psutil.virtual_memory().total / 1024 / 1024 / 1024).quantize(Decimal("0.01"),
                                                                                                    rounding="ROUND_HALF_UP"),
                "MemoryUsageRate": Decimal(psutil.virtual_memory().used / 1024 / 1024 / 1024).quantize(Decimal("0.01"),
                                                                                                       rounding="ROUND_HALF_UP"),
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
            "data": {
                "title": {
                    "text": "cpu核心使用率",
                    "x": "center",
                    "textStyle": {
                        "fontSize": 14
                    }
                },
                "tooltip": {
                    "trigger": "axis"
                },
                "legend": {
                    "data": [
                        "",
                        ""
                    ]
                },
                "xAxis": [
                    {
                        "type": "category",
                        "boundaryGap": "false",
                        "data": [
                            "06:00",
                            "06:30",
                            "07:00",
                            "07:30",
                            "08:00",
                            "08:30",
                            "09:00",
                            "09:30",
                            "10:00",
                            "11:30",
                            "12:00",
                            "12:30",
                            "13:00",
                            "13:30",
                            "14:00",
                            "14:30",
                            "15:00",
                            "15:30",
                            "16:00",
                            "16:30",
                            "17:00",
                            "17:30",
                            "18:00",
                            "18:30",
                            "19:00",
                            "19:30",
                            "20:00",
                            "20:30",
                            "21:00",
                            "21:30",
                            "22:00",
                            "22:30",
                            "23:00",
                            "23:30"
                        ]
                    }
                ],
                "yAxis": [
                    {
                        "type": "value"
                    }
                ],
                "series": [
                    {
                        "name": "PV",
                        "type": "line",
                        "smooth": "true",
                        "itemStyle": {
                            "normal": {
                                "areaStyle": {
                                    "type": "default"
                                }
                            }
                        },
                        "data": [
                            111,
                            222,
                            333,
                            444,
                            555,
                            666,
                            3333,
                            33333,
                            55555,
                            66666,
                            33333,
                            3333,
                            6666,
                            11888,
                            26666,
                            38888,
                            56666,
                            42222,
                            39999,
                            28888,
                            17777,
                            9666,
                            6555,
                            5555,
                            3333,
                            2222,
                            3111,
                            6999,
                            5888,
                            2777,
                            1666,
                            999,
                            888,
                            777
                        ]
                    },
                    {
                        "name": "UV",
                        "type": "line",
                        "smooth": "true",
                        "itemStyle": {
                            "normal": {
                                "areaStyle": {
                                    "type": "default"
                                }
                            }
                        },
                        "data": [
                            11,
                            22,
                            33,
                            44,
                            55,
                            66,
                            333,
                            3333,
                            5555,
                            12666,
                            3333,
                            333,
                            666,
                            1188,
                            2666,
                            3888,
                            6666,
                            4222,
                            3999,
                            2888,
                            1777,
                            966,
                            655,
                            555,
                            333,
                            222,
                            311,
                            699,
                            588,
                            277,
                            166,
                            99,
                            88,
                            77
                        ]
                    }
                ]
            }
        })
