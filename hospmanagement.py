from DoctorClass import Doctor
from PatientClass import Patient
import threading
from Assignment import assignment
import json

doctors_list = []
patients_list = []


while True:
    print("1> Create Doctor")
    print("2> Enter Patient")
    print("3> Get bill of a Patient")
    print("4> Exit")
    op = int(input())

    try:
        if op == 1:
            doctor = Doctor(
                "Dr." + input("Enter the name: "), int(input("Enter the fee: "))
            )
            doctors_list.append(doctor)

        elif op == 2:
            patient = Patient(
                input("Enter patient's id: "),
                input("Enter patient's name: "),
                int(input("Enter patient's age: ")),
                input("Enter patient's problem: "),
                int(input("Enter patient's the duration: ")),
            )
            patients_list.append(
                patient.details()
            )  # details() - returns a dict with details, Next step to append this in JSON file

            thread = threading.Thread(
                target=assignment, args=(patient, doctors_list)
            )  # Should increment bills and visits
            thread.start()

            with open("History.json", "a") as f:
                json.dump(patient.details(), f)

        elif op == 3:
            print("Enter the patient's id: ")
            pid = input()
            f = open("History.json")
            for patient in json.load(f):  # To traverse a list with Dictionary elements
                if patient.id == pid:
                    print(sum(patient.bill))
                    break
            f.close()
    except:
        break
    if op == 4:
        print("Exiting......")
        break

    print()
