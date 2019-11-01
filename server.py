from flask import Flask, render_template, request, redirect
from jinja2 import StrictUndefined
from model import connect_to_db, db, Doctor, Patient, Appointment

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined

##########################################################################

@app.route('/')
@app.route('/doctors', methods=['GET'])
def index():
    """Get a list of doctors"""

    doctors = Doctor.query.all()

    return render_template('doctor_list.html', doctors=doctors)


@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def doctor_detail(doctor_id):
    """Show appointment form"""

    doctor = Doctor.query.get(doctor_id)
   
    return render_template('appointment_form.html')


@app.route('/appointment', methods=['GET'])
def appointment_list():
    """Show a list of appointment"""

    appointments = Appointment.query.all()

    return render_template('appointment_list.html', appointments=appointments)


@app.route('/appointment', methods=['POST'])
def make_appointment():
    """Add new appointment"""

    fname = request.form['fname']
    lname = request.form['lname']
    patient_type = request.form['patient_type']
    appointment_time = request.form['appointment_time']

    new_patient = Patient(fname=fname, lname=lname, patient_type=patient_type, 
                          appointment_time=appointment_time)
    db.session.add(new_patient)
    db.session.commit()

    return redirect('/appointment')


#########################################################################

if __name__ == "__main__":

    app.debug = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.run(port=5000, host='0.0.0.0')










