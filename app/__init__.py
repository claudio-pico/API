import flask

import json

import Procesos, Constantes

app = flask.Flask(__name__)


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
    if (not flask.request.json or not 'pid' in flask.request.json):
        mensaje = {'Mensaje': Constantes.ingreseDatos}
        return response(mensaje, 400)
    pid = int(flask.request.json['pid'])
    data = Procesos.matarProcesos(pid)
    if data == Constantes.noExistePorceso:
        mensaje = {'Mensaje': data, 'PID': pid}
        return response(mensaje,404)

    return response(data,200)


@app.route("/Process", methods=['PUT'])
def repriorizar():
    if (not flask.request.json or not 'NI' in flask.request.json) or (not 'pid' in flask.request.json):
        mensaje = {'Mensaje': Constantes.ingreseDatos}
        return response(mensaje,400)

    intNI = int(flask.request.json['NI'])
    pid = int(flask.request.json['pid'])
    if intNI < -20 or intNI > 20:
        mensaje = {'Mensaje': 'prioridades -20 hasta 20', 'PID': pid}
        return response(mensaje,400)

    data = Procesos.repriorizarProceso(pid, intNI)
    if data == Constantes.noExistePorceso:
        mensaje = {'Mensaje': data, 'PID': flask.request.json['pid']}
        return response(mensaje,404)
    return response(data,200)


@app.route("/Process", methods=['POST'])
def lanzar():
    if not flask.request.json or not 'programa' in flask.request.json:
        mensaje = {'Mensaje':Constantes.ingreseDatos}
        return response(mensaje,404)
    data = Procesos.lanzarProcesos(flask.request.json['programa'])
    mensaje = {'Process': flask.request.json['programa']}
    return response(mensaje,200)

def response(data,code):
    r = flask.make_response(json.dumps(data), code)
    r.mimetype = 'application/json'
    return r

if __name__ == "__main__":
    app.run()
