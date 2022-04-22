from random import randint, choice  # choice for gender
from abc import ABC
import threading
from Assignment import assignment
from Operations import generate_id

problems_list = ["Headache", "Fever", "Dialysis", "Bloodwork", "Fracture"]
gender_list = ["Male", "Female"]


# Adding Persons - Doctors/Patients from user
def create_person(option, doctors_list, patients_list):
    if option == 1:
        doctor = Doctor("Dr." + input("Enter the name: "))
        doctors_list.append(doctor)

    elif option == 2:
        patient = Patient(
            input("Enter patient's id: "),
            input("Enter patient's name: "),
        )
        patients_list.append(patient.details())

        thread = threading.Thread(
            target=assignment, args=(patient, doctors_list)
        )  # Should increment bills and visits
        thread.start()


class Person(ABC):
    def __init__(self, name):
        self.name = name
        self.age = randint(30, 60)
        self.gender = choice(gender_list)


class Patient(Person):
    def __init__(self, id, name):
        super().__init__(name)
        if id == "none":
            self.id = generate_id(self.name, self.age)
        else:
            self.id = id
        self.problem = choice(problems_list)
        self.bills = []
        self.problems_list = []
        self.problems_list.insert(0, self.problem)
        self.time_per_visits = []  # Durations
        self.duration = randint(5, 10)
        self.time_per_visits.insert(0, self.duration)
        self.visited_by_doc = []

    def __str__(self):
        print("Patient Details")
        return "ID: {}\t Name: {}\t Gender: {}\t Age: {}\t\n".format(
            self.id, self.name, self.gender, self.age
        )

    def details(self):
        return {
            "name": self.name,
            "id": self.id,
            "age": self.age,
            "gender": self.gender,
            "problem": self.problems,
            "time_per_visits": self.time_per_visits,
            "bills": self.bills,
            "visited_by_doc": self.visited_by_doc,
        }


class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.fee = randint(1, 8) * 100
        self.isfree = True

    def __str__(self):
        print("Doctor Details")
        return "Name: {}\t Gender: {}\t Age: {}\t Fee: {}\t\n".format(
            self.name, self.gender, self.age, self.fee
        )
