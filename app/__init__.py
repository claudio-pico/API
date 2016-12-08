from flask import Flask, abort, make_response

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


@app.route("/Process/<int:pid>/<string:NI>", methods=['PUT'])
def repriorizar(pid, NI):
    intNI = int(NI)
    if intNI < -20 or intNI > 20:
        mensaje = {'Mensaje': 'prioridades -20 hasta 20', 'PID': pid}
        return make_response(json.dumps(mensaje), 404)
    data = Procesos.repriorizarProceso(pid, intNI)
    if data == Constantes.noExistePorceso:
        mensaje = {'Mensaje': data, 'PID': pid}
        return make_response(json.dumps(mensaje), 404)

    return json.dumps(data)


@app.route("/Process/<string:programa>", methods=['POST'])
def lanzar(programa):
    data = Procesos.lanzarProcesos(programa)
    mensaje = {'Porceso': programa}
    return json.dumps(mensaje)


if __name__ == "__main__":
    app.run()
