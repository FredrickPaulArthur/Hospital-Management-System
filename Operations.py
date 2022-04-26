from json import load

# Must return None if no doctors are available after one iteration
def available_doc(doctors, name):  # TODO: make it Asynchronous
    while True:
        for doc in doctors:
            if doc.isfree:
                doc.isfree = False
                return doc  # Iterates with 1sec intervals until one Doctor is free
        break
        return None
        # time.sleep(1)


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
                    print(this_visit["bill"])
                break


def erase_file(file_name):
    with open(file_name, "r+") as f:  # opens file in read and write mode
        f.truncate()


def generate_id(name, age):
    id = name + str(age)
    return id
