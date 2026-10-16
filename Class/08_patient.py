class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def total_bill(self, medicine_charges=0, test_charges=0):
        return self.consultation_fee + medicine_charges + test_charges

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee: Rs.", self.consultation_fee)


patient = Patient(201, "Neha", 25, "Fever", 500)
patient.display()
medicine = float(input("Enter medicine charges: Rs. "))
tests = float(input("Enter test charges: Rs. "))
print("Total Bill: Rs.", patient.total_bill(medicine, tests))
