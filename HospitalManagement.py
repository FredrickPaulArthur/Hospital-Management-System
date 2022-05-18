from Persons import Doctor, Patient
from Operations import calculate_bill, erase_file
import threading

erase_file("Results.txt")
erase_file("History.json")

doctors_list = []
patients_list = []  # Class objects list
waiting_queue = []

while True:
    print("\n1> Enter Doctor")  # Doctor enters and looks for patient
    print("2> Enter Patient")  # Patient enters and looks for available doctor
    print("3> Get bill of a Patient")
    print("4> Exit program")
    try:
        option = int(input("Option: "))
        if option not in range(1, 5):
            raise ValueError
    except ValueError:
        print("\nPlease enter a correct option\n")
        continue

    # update_history(patients_list)

    if option == 1:
        Doctor.create_doctor(doctors_list, patients_list, waiting_queue)

    elif option == 2:
        Patient.create_patient(doctors_list, patients_list, waiting_queue)

    elif option == 3:
        calculate_bill()

    elif option == 4:  # To exit and to update history for the day
        # To join() if any Threads are running - skipping the main Thread
        # threading.enumerate returns a list of Currently running threads including the main threads
        if len(threading.enumerate()) > 1:
            print("\nExiting, waiting for the final patients.....")
            while len(threading.enumerate()) > 1:
                threading.enumerate()[1].join()
        else:
            print("\nExited")
        break
