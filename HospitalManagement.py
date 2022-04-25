from PersonClass import Person  # create_person
from Operations import update_history, calculate_bill, erase_file
import threading

erase_file("Results.txt")
erase_file("History.json")

doctors_list = []
patients_list = []

while True:
    print("1> Create Doctor")
    print("2> Enter Patient")
    print("3> Get bill of a Patient")
    print("4> Exit program")
    option = int(input())
    update_history(patients_list)

    # Adding People
    if option == 1 or option == 2:
        Person.create_person(option, doctors_list, patients_list)

    # Bill Calculation
    elif option == 3:
        calculate_bill()

    # Exiting
    elif option == 4:  # To exit and to update history for the day
        print("Exiting, waiting to close.....")
        # To join() if any Threads are running
        while len(threading.enumerate()) > 1:  # Skipping the main Thread
            threading.enumerate()[1].join()
        break
    print()

update_history(patients_list)
