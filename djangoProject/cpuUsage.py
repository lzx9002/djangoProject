import time
from psutil import virtual_memory, cpu_percent

histories = {
    "time": [],
    "cpu": [],
    "memory": []
}

for n in range(0, 600):
    histories["time"].append('')
    histories["cpu"].append(0)
    histories["memory"].append(0)


def cpuUsableRecorder():
    while True:
        if len(histories["time"]) > 600:
            del histories["time"][0]
            del histories["cpu"][0]
            del histories["memory"][0]
        histories["cpu"].append(cpu_percent(interval=1))
        histories["memory"].append(virtual_memory().percent)
        histories["time"].append(time.strftime("%H:%M:%S", time.localtime()))
