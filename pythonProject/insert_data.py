from app import db, Patient, Doctor, Appointment, Payment

# Add sample data
patient = Patient(name='John Doe', age=40, medical_history='None')
doctor = Doctor(name='Dr. Smith', specialization='Cardiology')
appointment = Appointment(patient_id=1, doctor_id=1, date='2025-02-01', reason='Routine check-up')
payment = Payment(amount=100.0, method='Credit Card', date='2025-02-01')

db.session.add(patient)
db.session.add(doctor)
db.session.add(appointment)
db.session.add(payment)