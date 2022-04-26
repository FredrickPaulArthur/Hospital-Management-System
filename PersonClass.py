from random import randint, choice  # choice for gender
from abc import ABC
import threading
from Assignment import assignment
from Operations import generate_id
from Operations import available_doc

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

    def create_person(option, doctors_list, patients_list, waiting_queue):
        if option == 1:
            doctor = Doctor("Dr." + input("Enter the name: "))
            doctors_list.append(doctor)
        elif option == 2:
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
                    return

            # If doctor is available, the thread starts. If not, patient is sent to the WaitingQueue
            avl_doc = available_doc(doctors_list, patient.name)
            if avl_doc is not None:
                thread = threading.Thread(
                    target=assignment, args=(patient, avl_doc, waiting_queue)
                )
                thread.start()
            else:
                waiting_queue.append(patient)


class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.isfree = True


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

    def details(self):
        return {
            "name": self.name,
            "id": self.id,
            "age": self.age,
            "gender": self.gender,
            "visit_details": self.visit_details,
        }
