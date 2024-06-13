import time, threading
from dependencies.Operations import available_doc, update_history, check_waiting_queue

problems_dict = {
    "Headache": 300,
    "Fever": 200,
    "Dialysis": 400,
    "Bloodwork": 100,
    "Fracture": 350,
    "Eye-checkup": 450,
}

# Comes from create_patient
def assign_doctor(patient, doctors_list, waiting_queue, patients_list):
    avl_doc = available_doc(doctors_list)
    if avl_doc is not None:
        thread = threading.Thread(
            target=treatment, args=(patient, avl_doc, patients_list, waiting_queue)
        )
        thread.start()

    else:
        with open("results.txt", "a") as f:
            f.write("\nPatient {} added to waiting_queue\n".format(patient.name))
        waiting_queue.append(patient)
        patient.inqueue = True


def treatment(patient, avl_doc, patients_list, waiting_queue):
    avl_doc.isfree = False
    patient.isattending = True
    f = open("results.txt", "a")
    f.write("\nPatient {} is attending".format(patient.name))
    f.write(
        "\n{} on-duty with {} for {}mins.....\n".format(
            avl_doc.name, patient.name, patient.visit_details[-1]["duration"]
        )
    )
    f.close()

    time.sleep(patient.visit_details[-1]["duration"])  # ----------------------Treatment

    this_visit = patient.visit_details[-1]
    this_visit["visited_by_doc"] = avl_doc.name
    this_visit["bill"] = problems_dict[this_visit["problem"]]
    with open("results.txt", "a") as f:
        f.write("\nPatient {} exited, {} is free\n".format(patient.name, avl_doc.name))

    avl_doc.isfree = True
    patient.isattending = False
    patient.inqueue = False
    update_history(patients_list)

    check_waiting_queue(avl_doc, waiting_queue, treatment, patients_list)
