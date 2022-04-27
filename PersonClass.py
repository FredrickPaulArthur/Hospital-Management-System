from random import randint, choice  # choice for gender
from abc import ABC
from Assignment import treatment
import threading
from Operations import generate_id, check_waiting_queue  # , available_doc

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

    # For Encapsulation
    # Must return None if no doctors are available after one iteration
    def available_doc(doctors):  # TODO: make it Asynchronous
        for doc in doctors:
            if doc.isfree:
                doc.isfree = False
                return doc
        # time.sleep(1)

    def create_doctor(doctors_list, waiting_queue):
        doctor = Doctor("Dr." + input("Enter the name: "))
        doctors_list.append(doctor)
        # The Doctor who has just arrived will check for Patients in the Queue

        if len(waiting_queue) > 0:
            check_waiting_queue(waiting_queue.pop(0), doctor, waiting_queue)


class Patient(Person):
    def __init__(self, name):
        super().__init__(name)
        self.id = generate_id(self.name, self.age)
        self.visit_details = []
        self.visit_details.append(
            {
                "duration": randint(8, 13),
                "visited_by_doc": "null",
                "problem": choice(list(problems_dict)),
                "bill": 0,
            }
        )

    # For Encapsulation
    def create_patient(doctors_list, patients_list, waiting_queue):
        id = input("Enter patient's id: ")
        name = input("Enter patient's name: ")
        if id == "none":
            # New Patient
            patient = Patient(name)
            patients_list.append(patient)
        elif id != "none":
            # Check if ID already exists in the patients_list
            for patient in patients_list:
                if patient.id == id:
                    patient.visit_details.append(
                        {
                            "duration": randint(8, 13),
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
        # If doctor is available, the thread starts. If not, patient is sent to the WaitingQueue
        avl_doc = Doctor.available_doc(doctors_list)
        # check_waiting_queue(patient, avl_doc, waiting_queue)
        if avl_doc is not None:
            thread = threading.Thread(
                target=treatment, args=(patient, avl_doc, waiting_queue)
            )
            thread.start()
        else:
            waiting_queue.append(patient)

    def details(self):
        return {
            "name": self.name,
            "id": self.id,
            "age": self.age,
            "gender": self.gender,
            "visit_details": self.visit_details,
        }
