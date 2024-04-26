import platform
import django
import psutil
import os
from decimal import Decimal
from django.http import JsonResponse
from djangoProject.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL
from .uploads import getNewName
from django.views.decorators.csrf import csrf_exempt
from api.models import User_name_list
from .cpuUsage import histories


# Create your views here.


@csrf_exempt
# 接收请求数据
def login_api(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        rows = User_name_list.objects.filter(password=password, username=name)
        if rows:
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
    return JsonResponse({
        "ode": -1,
        "msg": "用户名或密码错误"
    })


@csrf_exempt
def userinfo(request):
    if request.method == 'GET':
        try:
            token = request.GET['token']
        except KeyError:
            pass
        else:
            rows = User_name_list.objects.filter(username=token)
            if rows:
                return JsonResponse({
                    "code": 0,
                    "msg": "",
                    "data": {
                        "role": rows[0].role.id,
                        "username": token,
                        "user": rows[0].nickname,
                        "sex": rows[0].sex,
                        "avatar": rows[0].avatar,
                        "cellphone": rows[0].cellphone,
                        "email": rows[0].email,
                        "remarks": rows[0].remarks,

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
    if request.method == 'GET':
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
    if request.method == 'GET':
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
    if request.method == 'GET':
        return JsonResponse({
            "code": 0,
            "msg": "",
            "data": histories
        })


def userList(request):
    if request.method == 'GET':
        rows = User_name_list.objects.all()
        user_list = {
            "code": 0,
            "msg": "",
            "data": []
        }
        for user in rows:
            user_list["data"].append({
                "id": user.id,
                "username": user.nickname,
                "avatar": user.avatar,
                "phone": user.cellphone,
                "email": user.email,
                "sex": user.sex,
                "jointime": user.jointime,
            })
        return JsonResponse(user_list)


def upload_avatar(request):
    if request.method == 'POST':
        name = request.POST['token']
        # 获取一个文件管理器对象
        file = request.FILES['file']
        file_type = file.name.split('.')[-1]
        # 保存文件
        new_name = getNewName('avatar', user=name, file_type=file_type)  # 具体实现在自己写的uploads.py下
        # 将要保存的地址和文件名称
        where = '%s/users/%s' % (MEDIA_ROOT, new_name)
        # 分块保存image
        content = file.chunks()
        with open(where, 'wb') as f:
            for i in content:
                f.write(i)
        # 返回的httpresponse
        return JsonResponse({
            "code": 0,
            "msg": "",
            "data": {
                "url": "/%s%susers/%s" % (STATIC_URL, MEDIA_URL, new_name),
            }
        })


def upload_user_info(request) :
    if request.method == 'POST':
        username = request.POST['token']
        rows = User_name_list.objects.filter(username=username)
        nickname = request.POST['nickname']
        sex = request.POST['sex']
        avatar = request.POST['avatar']
        cellphone = request.POST['cellphone']
        email = request.POST['email']
        try:
            remarks = request.POST['remarks']
        except KeyError:
            remarks = rows[0].remarks
        rows.update(
            nickname=nickname,
            sex=sex,
            avatar=avatar,
            cellphone=cellphone,
            email=email,
            remarks=remarks,
        )
        return JsonResponse({
            "code": 0,
            "msg": "",
            "data": {}
        })
