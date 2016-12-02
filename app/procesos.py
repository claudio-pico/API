import json

import datetime
import psutil


def listaProcesos():
    data = []
    listProcesos = []
    for process in psutil.process_iter():
        proceso = {}
        proceso["%CPU"] = "{0:.2f}".format(process.cpu_percent())
        proceso["%MEM"] = "{0:.2f}".format(process.memory_percent())
        proceso["status"] = str(process.status())
        proceso["isRunning"] = process.is_running()
        proceso["Usuario"] = process.username()
        proceso["Nombre"] = process.name()
        # proceso["PPIDD"] = process.ppid
        proceso["PID"] = process.pid
        listProcesos.append(proceso)
    jsonProcesos = {"Procesos": listProcesos}
    return jsonProcesos
