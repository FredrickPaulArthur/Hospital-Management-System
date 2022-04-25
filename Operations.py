from json import load


def update_history(patients_list):
    with open("History.json", "r+") as f:
        f.truncate()
        f.write(str(patients_list).replace("'", '"'))
        # To replace (') -> (") for JSON


def calculate_bill():
    print("Enter the patient's id: ")
    pid = input()
    with open("History.json", "r") as f:
        # To traverse the file with Dictionary elements and locate the ID
        for patient in load(f):
            if patient["id"] == pid:
                if len(patient["bills"]) == 0:
                    print("Patient still in treatment.")
                else:
                    # or print("Total Bill: ", sum(patient["bills"]))
                    print(patient["bills"][0])
                break


def erase_file(file_name):
    with open(file_name, "r+") as f:  # opens file in read and write mode
        f.truncate()


def generate_id(name, age):
    id = name + str(age)
    return id
