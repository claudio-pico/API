from flask import Flask, abort, make_response, request

import json

import Procesos, Constantes

app = Flask(__name__)


@app.route("/Processes")
def listar():
    data = Procesos.listaProcesos()
    return response(data, 200)


@app.route("/Process/<int:pid>")
def listarProceso(pid):
    data = Procesos.listaProcesos(pid)
    if data == Constantes.noExistePorceso:
        mensaje = {'Mensaje': data, 'PID': pid}
        return response(mensaje,404)

    return response(data,200)


@app.route('/Process', methods=['DELETE'])
def matar():
    if (not request.json or not 'pid' in request.json):
        mensaje = {'Mensaje': Constantes.ingreseDatos}
        return response(mensaje, 400)
    pid = int(request.json['pid'])
    data = Procesos.matarProcesos(pid)
    if data == Constantes.noExistePorceso:
        mensaje = {'Mensaje': data, 'PID': pid}
        return response(mensaje,404)

    return response(data,200)


@app.route("/Process", methods=['PUT'])
def repriorizar():
    if (not request.json or not 'NI' in request.json) or (not 'pid' in request.json):
        mensaje = {'Mensaje': Constantes.ingreseDatos}
        return response(mensaje,400)

    intNI = int(request.json['NI'])
    pid = int(request.json['pid'])
    if intNI < -20 or intNI > 20:
        mensaje = {'Mensaje': 'prioridades -20 hasta 20', 'PID': pid}
        return response(mensaje,400)

    data = Procesos.repriorizarProceso(pid, intNI)
    if data == Constantes.noExistePorceso:
        mensaje = {'Mensaje': data, 'PID': request.json['pid']}
        return response(mensaje,404)
    return response(data,400)


@app.route("/Process", methods=['POST'])
def lanzar():
    if not request.json or not 'programa' in request.json:
        mensaje = {'Mensaje':Constantes.ingreseDatos}
        return response(mensaje,404)
    data = Procesos.lanzarProcesos(request.json['programa'])
    mensaje = {'Process': request.json['programa']}
    return response(mensaje,200)

def response(data,code):
    r = make_response(json.dumps(data),code)
    r.mimetype = 'application/json'
    return r

if __name__ == "__main__":
    app.run()
