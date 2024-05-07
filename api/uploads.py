import time

import numpy as np


def getNewName(file_name, user, file_type):
    # 前面是file_type+年月日时分秒
    new_name = time.strftime(file_name + '-' + user + '-%Y%m%d%H%M%S', time.localtime())
    # 最后是5个随机数字
    # Python中的numpy库中的random.randint(a, b, n)表示随机生成n个大于等于a，小于b的整数
    ranList = np.random.randint(0, 10, 5)
    for i in ranList:
        new_name += str(i)
    # 加后缀名
    new_name += '.' + file_type
    # 返回字符串
    return new_name


def Request_processing(request):
    request_list = str(request, encoding="gbk").split('&')
    for i in request_list:
        request_json_list = i.split('=')
        request.POTS[request_json_list[0]] = request_json_list[1]
    return request
