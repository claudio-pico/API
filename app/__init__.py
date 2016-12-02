from flask import Flask
import json
import procesos

app = Flask(__name__)


@app.route("/")
def hello():
    data = procesos.listaProcesos()
    return json.dumps(data)


# @app.route("/listarProcesos")
# def listarProcesos():
# return json.dumps(procesos.listarProcesos())


if __name__ == "__main__":
    app.run()
