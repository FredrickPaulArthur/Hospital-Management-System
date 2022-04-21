import time


def availableDoc(doctors):  # TODO: Edit with Asynchronous function
    while True:
        for doc in doctors:
            if doc.isfree:
                doc.isfree = False
                return doc  # Iterates with 1sec intervals until one Doctor is free
        time.sleep(1)


def assignment(patient, doctors_list):
    avl_doc = availableDoc(doctors_list)  # returns None if no docs available?

    if (
        avl_doc is not None
    ):  # Must return None if no doctors are available after one iteration
        with open("results.txt", "a") as f:
            f.write(
                "\n{} on-duty with {} for {}mins.....".format(
                    avl_doc.name, patient.name, patient.duration
                )
            )
        # print(
        #     "\n{} on-duty with {} for {}mins.....".format(
        #         avl_doc.name, patient.name, patient.duration
        #     )
        # )
        time.sleep(patient.duration)
        with open("results.txt", "a") as f:
            f.write(
                "\nPatient {} exited, {} is free\n".format(patient.name, avl_doc.name)
            )
        avl_doc.isfree = True
