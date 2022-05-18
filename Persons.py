from random import randint, choice  # choice for gender
from abc import ABC
from Assignment import assign_doctor, treatment
from Operations import generate_id, check_waiting_queue


problems_dict = {
    "Headache": 300,
    "Fever": 200,
    "Dialysis": 400,
    "Bloodwork": 100,
    "Fracture": 350,
    "Eye-checkup": 450,
}


class Person(ABC):
    def __init__(self, name):
        self.name = name
        self.age = randint(30, 60)
        self.gender = choice(["Male", "Female"])


class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.isfree = True

    def create_doctor(doctors_list, patients_list, waiting_queue):
        doctor = Doctor("Dr." + input("Enter the name: "))
        doctors_list.append(doctor)
        # The Doctor who has just arrived will check for Patients in the Queue
        check_waiting_queue(doctor, waiting_queue, treatment, patients_list)


class Patient(Person):
    def __init__(self, name):
        super().__init__(name)
        self.id = generate_id(self.name, self.age)
        self.isattending = False
        self.inqueue = False
        self.visit_details = []
        self.visit_details.append(
            {
                "duration": randint(10, 15),
                "visited_by_doc": "null",
                "problem": choice(list(problems_dict)),
                "bill": 0,
            }
        )

    def details(self):
        return {
            "name": self.name,
            "id": self.id,
            "age": self.age,
            "gender": self.gender,
            "visit_details": self.visit_details,
        }

    def create_patient(doctors_list, patients_list, waiting_queue):
        id = input("Enter patient's id: ")
        if id == "none":
            # New Patient
            name = input("Enter patient's name: ")
            patient = Patient(name)
            patients_list.append(patient)
        elif id != "none":
            # Check if ID already exists in the patients_list
            for patient in patients_list:
                if patient.id == id:
                    if patient.isattending:
                        print("\nPatient is still attending\n")
                        return
                    elif patient.inqueue:
                        print("\nPatient already in the Waiting Queue\n")
                        return
                    else:
                        patient.visit_details.append(
                            {
                                "duration": randint(10, 15),
                                "visited_by_doc": "null",
                                "problem": choice(list(problems_dict)),
                                "bill": 0,
                            }
                        )
                    break
            else:
                # Invalid Patient ID
                print("\nEnter a valid Patient Id\n")
                return

        assign_doctor(patient, doctors_list, waiting_queue, patients_list)
