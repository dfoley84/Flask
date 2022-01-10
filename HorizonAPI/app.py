from enum import unique
from click.core import fast_exit
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from rabbitmq import Delete_VDesk
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:test//@/FLASK'
swagger = Swagger(app)
db = SQLAlchemy(app)


class vDesk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ConnectionBroker = db.Column(db.String(120), unique=False)
    VDIPool = db.Column(db.String(120), unique=False)
    MachineName = db.Column(db.String(120), unique=True)
    MachineStatus = db.Column(db.String(120), unique=False)
    AgentVersion = db.Column(db.Integer, unique=False)
    OSVersion = db.Column(db.String(120), unique=False)

    @property
    def serialize(self):
        # Returns Data Object In Proper Format
        return {
            'ConnectionBroker': self.ConnectionBroker,
            'VDIPool': self.VDIPool,
            'MachineName': self.MachineName,
            'MachineStatus': self.MachineStatus,
            'AgentVersion': self.AgentVersion,
            'OSVersion': self.OSVersion
        }

@app.route('/vdesk', methods=['GET'])
@swag_from("./vdesk.yaml")
def vdesk():
    return jsonify(vDesks = [i.serialize for i in vDesk.query.all()])

@app.route('/vdesk/MachineName/<string:machinename>', methods=['GET'])
@swag_from("./vdeskname.yaml")
def GetMachineName(machinename):
    return jsonify(vDesk = [i.serialize for i in vDesk.query.filter_by(MachineName=machinename).all()])


@app.route('/vdesk/Status/<string:status>', methods=['GET'])
@swag_from("./vdeskstatus.yaml")
def GetMachineStatus(status):
    return jsonify(vDesks = [i.serialize for i in vDesk.query.filter_by(MachineStatus='Connected').all()])


@app.route('/vdesk/<string:machinename>',methods=['DELETE'])
@swag_from("./DeleteMachine.yaml")
def DeleteMachineName(machinename):
    data = []
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run()



