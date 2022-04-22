import time

problems_dict = {
    "Headache": 300,
    "Fever": 200,
    "Dialysis": 400,
    "Bloodwork": 100,
    "Fracture": 350,
}

# Must return None if no doctors are available after one iteration
def available_doc(doctors):  # TODO: make it Asynchronous
    while True:
        for doc in doctors:
            if doc.isfree:
                doc.isfree = False
                return doc  # Iterates with 1sec intervals until one Doctor is free
        time.sleep(1)


def assignment(patient, doctors_list):
    avl_doc = available_doc(doctors_list)  # returns None if no docs available?

    # Waits until Doctor is available
    if avl_doc is not None:
        with open("results.txt", "a") as f:
            f.write(
                "\n{} on-duty with {} for {}mins.....\n".format(
                    avl_doc.name, patient.name, patient.duration
                )
            )
        time.sleep(patient.duration)
        patient.bills.insert(0, problems_dict[patient.problem])
        patient.visited_by_doc.insert(0, avl_doc.name)
        # Update details like - bills, visited_by_doc(DocName)
        with open("results.txt", "a") as f:
            f.write(
                "\nPatient {} exited, {} is free\n".format(patient.name, avl_doc.name)
            )
        avl_doc.isfree = True
