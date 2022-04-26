from PersonClass import Person
from Operations import update_history, calculate_bill, erase_file
import threading

erase_file("Results.txt")
erase_file("History.json")

doctors_list = []
patients_list = []  # Class objects list
waiting_queue = []

while True:
    print("1> Create Doctor")
    print("2> Enter Patient")
    print("3> Get bill of a Patient")
    print("4> Exit program")
    try:
        option = int(input("Option: "))
    except ValueError:
        print("\nPlease enter a correct option\n")
        continue

    update_history(patients_list)

    # Adding People
    if option == 1 or option == 2:
        Person.create_person(option, doctors_list, patients_list, waiting_queue)

    # Bill Calculation
    elif option == 3:
        calculate_bill()

    # Exiting
    elif option == 4:  # To exit and to update history for the day
        # To join() if any Threads are running - skipping the main Thread
        # threading.enumerate returns a list of Currently running threads including the main threads
        if len(threading.enumerate()) > 1:
            print("Exiting, waiting for the final patients.....")
            while len(threading.enumerate()) > 1:
                threading.enumerate()[1].join()
        else:
            print("Exited")
        break
    print()

update_history(patients_list)
