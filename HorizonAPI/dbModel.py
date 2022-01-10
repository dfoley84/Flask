from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

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
