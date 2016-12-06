from flask import Flask, abort , make_response

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
    if data==Constantes.noExistePorceso or data==Constantes.noTienePermiso:
        mensaje={'Mensaje':data,'PID':pid}
        return make_response(json.dumps(mensaje), 404)

    return json.dumps(data)

if __name__ == "__main__":
    app.run()
