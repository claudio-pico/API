import json

import datetime
import psutil


def listaProcesos():
    data = []
    listProcesos = []
    for process in psutil.process_iter():
        proceso = {}

        proceso["TIME"] = process.cpu_times()[1]

        proceso["START"] = datetime.datetime.fromtimestamp(process.create_time()).strftime("%Y-%m-%d %H:%M:%S")

        #terminal que controla el proceso (tty)
        proceso["TTY"] = process.terminal()

        proceso["%CPU"] = "{0:.2f}".format(process.cpu_percent())

        #porcentaje de memoria fisica utilizada
        proceso["%MEM"] = "{0:.2f}".format(process.memory_percent())

        #resident set size, es la cantidad de memoria fisica no swappeada que la tareia a utilizado(kbit)
        proceso["RSS"] = process.memory_info()[0]

        #memoria virtual del proceso medida en KiB
        proceso["VSZ"] = process.memory_info()[1]

        proceso["status"] = str(process.status())

        proceso["isRunning"] = process.is_running()

        # usuario con el que se ejecuta el proceso
        proceso["Usuario"] = process.username()

        # Nombre del Proceso
        proceso["Nombre"] = process.name()

        # ID del porceso
        proceso["PID"] = process.pid
        listProcesos.append(proceso)
    jsonProcesos = {"Procesos": listProcesos}
    return jsonProcesos
