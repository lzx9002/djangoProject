import platform
import django
import psutil
from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from settings import MEDIA_ROOT
from .uploads import getNewName
from django.views.decorators.csrf import csrf_exempt
from api.models import User_name_list
from cpuUsage import histories


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
                        "avatar": "/static/media/users/%s" % rows[0].avatar.name,
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
                "avatar": "/static/media/users/%s" % user.avatar.name,
                "phone": user.cellphone,
                "email": user.email,
                "sex": user.sex,
                "jointime": user.jointime,
            })
        return JsonResponse(user_list)


def upload_avatar(request):
    if request.method == 'POST':
        # 获取一个文件管理器对象
        file = request.FILES['file']
        name = request.POST['token']

        # 保存文件
        new_name = getNewName('avatar')  # 具体实现在自己写的uploads.py下
        # 将要保存的地址和文件名称
        where = '%s/users/%s' % (MEDIA_ROOT, new_name)
        # 分块保存image
        content = file.chunks()
        with open(where, 'wb') as f:
            for i in content:
                f.write(i)

        # 上传文件名称到数据库
        User_name_list.objects.filter(username=name).update(avatar=new_name)
        # 返回的httpresponse
        return JsonResponse({
            "code": 0,
            "msg": "",
            "data": {
                "url": "/static/media/users/%s" % new_name,
            }
        })
