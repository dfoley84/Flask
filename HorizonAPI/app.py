from enum import unique
from click.core import fast_exit
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from rabbitmq import Delete_VDesk
from dbModel import vDesk
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:test//@/FLASK'
swagger = Swagger(app)
db = SQLAlchemy(app)


@app.route('/vdesk', methods=['GET'])
@swag_from("./yaml/vdesk.yaml")
def vdesk():
    return jsonify(vDesks = [i.serialize for i in vDesk.query.all()])


@app.route('/vdesk/MachineName/<string:machinename>', methods=['GET'])
@swag_from("./yaml/vdeskname.yaml")
def GetMachineName(machinename):
    return jsonify(vDesk = [i.serialize for i in vDesk.query.filter_by(MachineName=machinename).all()])


@app.route('/vdesk/Status/<string:status>', methods=['GET'])
@swag_from("./yaml/vdeskstatus.yaml")
def GetMachineStatus(status):
    return jsonify(vDesks = [i.serialize for i in vDesk.query.filter_by(MachineStatus='Connected').all()])


if __name__ == '__main__':
    app.run()




