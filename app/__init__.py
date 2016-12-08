from flask import Flask, abort, make_response, request

import json

import Procesos, Constantes

app = Flask(__name__)


@app.route("/Processes")
def listar():
    data = Procesos.listaProcesos()
    return json.dumps(data)


@app.route('/Process/<int:pid>', methods=['DELETE'])
def matar(pid):
    data = Procesos.matarProcesos(pid)
    if data == Constantes.noExistePorceso:
        mensaje = {'Mensaje': data, 'PID': pid}
        return make_response(json.dumps(mensaje), 404)

    return json.dumps(data)


@app.route("/Process", methods=['PUT'])
def repriorizar():
    if (not request.json or not 'NI' in request.json) or (not 'pid' in request.json):
        return make_response(json.dumps(Constantes.ingreseDatos), 404)

    intNI = int(request.json['NI'])
    pid = int(request.json['pid'])
    if intNI < -20 or intNI > 20:
        mensaje = {'Mensaje': 'prioridades -20 hasta 20', 'PID': pid}
        return make_response(json.dumps(mensaje), 404)

    data = Procesos.repriorizarProceso(pid, intNI)
    if data == Constantes.noExistePorceso:
        mensaje = {'Mensaje': data, 'PID': request.json['pid']}
        return make_response(json.dumps(mensaje), 404)

    return json.dumps(data)


@app.route("/Process", methods=['POST'])
def lanzar():
    if not request.json or not 'programa' in request.json:
        return make_response(json.dumps(Constantes.ingreseDatos), 404)
    data = Procesos.lanzarProcesos(request.json['programa'])
    mensaje = {'Process': request.json['programa']}
    return json.dumps(mensaje)


if __name__ == "__main__":
    app.run()
