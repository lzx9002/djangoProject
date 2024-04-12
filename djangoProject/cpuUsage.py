import pymysql
import time
from psutil import virtual_memory, cpu_percent
from djangoProject.settings import DATABASES

default = {
    'host': DATABASES['default']['HOST'],
    'user': DATABASES['default']['USER'],
    'password': DATABASES['default']['PASSWORD'],
    'port': DATABASES['default']['PORT'],
    'db': DATABASES['default']['NAME'],
    'charset': 'utf8',
}
conn = pymysql.connect(**default)
cur = conn.cursor()


def saveCpuUsage():
    cpu = cpu_percent(interval=1)
    memory = virtual_memory().percent
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql = "\
        INSERT INTO django.api_system_usage (time, cpu, memory) \
        VALUES ('%s', %s, %s)" % \
        (now_time, cpu, memory)
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
    except:
        conn.rollback()  # 如果发生错误则回滚
    # conn.close()  # 关闭数据库连接


def cpuUsableRecorder():
    while True:
        saveCpuUsage()
        time.sleep(8)
