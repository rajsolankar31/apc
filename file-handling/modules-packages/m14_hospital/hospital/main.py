from patient_management.patient import add_patient, get_patient
from doctor_management.doctor import get_doctor
from billing.bill import calculate_bill
from medical_records.records import add_record, get_records
add_patient(1, "Amit", 30); add_record(1, "Fever")
print(get_patient(1)); print(get_doctor(1)); print(get_records(1))
print("Bill:", calculate_bill(500, 350, 1200))
