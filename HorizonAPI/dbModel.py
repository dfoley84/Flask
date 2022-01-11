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
    user_id = db.Column(db.String(120), db.ForeignKey('UserName.id'), null=True)

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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(120), unique=False)
    Email = db.Column(db.String(140), unique=False)
    MachineName = db.relationship('vDesk', backref='user_id', lazy=True)
    @property
    def serialize(self):
        # Returns Data Object In Proper Format
        return {
            'UserName': self.UserName,
            'Email': self.Email,
            'MachineName': self.MachineName
        }
