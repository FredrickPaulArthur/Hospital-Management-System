from PersonClass import create_person
from Operations import update_history, calculate_bill, truncate_file

truncate_file("Results.txt")
truncate_file("History.json")
doctors_list = []
patients_list = []

while True:
    print("1> Create Doctor")
    print("2> Enter Patient")
    print("3> Get bill of a Patient")
    print("4> Exit")
    option = int(input())

    update_history(patients_list)
    # Adding People
    if option == 1 or option == 2:
        create_person(option, doctors_list, patients_list)
    # Bill Calculation
    elif option == 3:
        calculate_bill()
    # Exiting
    elif option == 4:  # To exit and to update history for the day
        print("Exiting, waiting to close.....")
        break
    print()
    update_history(patients_list)  # For what, threads to finish???


# Able to use as a list - YES
# with open("History.json", "r") as f:
#     a = json.load(f)
# print(type(a))
