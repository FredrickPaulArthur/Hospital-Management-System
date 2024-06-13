from json import load
import threading


def available_doc(doctors_list):
    for doc in doctors_list:
        if doc.isfree:
            doc.isfree = False
            return doc


def check_waiting_queue(doctor, waiting_queue, treatment, patients_list):
    if len(waiting_queue) > 0:
        thread = threading.Thread(
            target=treatment,
            args=(waiting_queue.pop(0), doctor, patients_list, waiting_queue),
        )
        thread.start()


def update_history(patients_list):
    details = []
    for obj in patients_list:
        details.append(obj.details())
    with open("History.json", "r+") as f:
        f.truncate()
        f.write(str(details).replace("'", '"'))
        # To replace (') -> (") for JSON


def calculate_bill():
    pid = input("Enter the patient's id: ")
    with open("History.json", "r") as f:
        # To traverse the file with Dictionary elements and locate the ID
        for patient_dict in load(f):
            if patient_dict["id"] == pid:
                this_visit = patient_dict["visit_details"][-1]
                if this_visit["bill"] == 0:
                    print("Patient still in treatment.")
                else:
                    # or print("Total Bill: ", sum(patient["bills"]))
                    print(
                        "The bill for {} is: ".format(patient_dict["name"]),
                        this_visit["bill"],
                    )
                break
        else:
            print("\nPlease Enter the correct ID")


def erase_file(file_name):
    with open(file_name, "r+") as f:  # opens file in read and write mode
        f.truncate()


def generate_id(name, age):
    id = name + str(age)
    return id
