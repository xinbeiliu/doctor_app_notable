from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

##########################################################################

class Doctor(db.Model):
    """Show doctor info"""

    __tablename__ = "doctors"

    doctor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(64), nullable=False)

    def __repr__(self):

            return f"""<Doctor doctor_id={self.doctor_id}"""


class Patient(db.Model):
    """Show patient info"""

    __tablename__ = "patients"

    patient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    patient_type = db.Column(db.String, nullable=False)
    appointment_time = db.Column(db.String(30), nullable=False)

    def __repr__(self):

            return f"""<Patient patient_id={self.patient_id}"""


class Appointment(db.Model):
    """Show appointment info"""

    __tablename__ = "appointments"

    appointment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.patient_id'), 
                           nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.doctor_id'), 
                           nullable=False)
    date_added = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    patients = db.relationship("Patient", backref=db.backref("appointments", 
                               order_by=appointment_id))
    doctors = db.relationship("Doctor", backref=db.backref("appointments", 
                               order_by=appointment_id))

    def __repr__(self):

            return f"""<Appointment appointment_id={self.appointment_id}
                        doctor_id={self.doctor_id}
                        patient_id={self.patient_id}"""

############################################################################

def connect_to_db(app, db_uri='postgresql:///doctorapp'):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    
    from server import app
    connect_to_db(app)
    print("Connected to DB.")



