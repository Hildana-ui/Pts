
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Patient, Doctor, Appointment, Payment
import qrcode




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    medical_history = db.Column(db.Text)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    specialization = db.Column(db.Text)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    date = db.Column(db.Date)
    reason = db.Column(db.String(100))

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    method = db.Column(db.String(50))
    date = db.Column(db.Date)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patients():
    patient = Patient.query.all()
    return render_template('patient.html')

@app.route('/admin')
def admin():
    appointments = Appointment.query.all()
    return render_template('admin.html')

@app.route('/generate_qr/<int:patient_id>')
def generate_qr(patient_id):
    patient = Patient.query.get(patient_id)
    qr_code = qrcode.make(f'Patient ID: {patient.id}\nName: {patient.name}')
    qr_code.save(f'static/qr_codes/{patient.id}.png')
    return redirect(url_for('patients'))
@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)





