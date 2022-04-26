import time, threading

problems_dict = {
    "Headache": 300,
    "Fever": 200,
    "Dialysis": 400,
    "Bloodwork": 100,
    "Fracture": 350,
    "Eye-checkup": 450,
}


def assignment(patient, avl_doc, waiting_queue):
    with open("results.txt", "a") as f:
        f.write("\nPatient {} is on top\n".format(patient.name))
    with open("results.txt", "a") as f:
        f.write(
            "\n{} on-duty with {} for {}mins.....\n".format(
                avl_doc.name, patient.name, patient.visit_details[-1]["duration"]
            )
        )
    time.sleep(patient.visit_details[-1]["duration"])  # ----------------------Treatment

    this_visit = patient.visit_details[-1]
    this_visit["visited_by_doc"] = avl_doc.name
    this_visit["bill"] = problems_dict[this_visit["problem"]]

    with open("results.txt", "a") as f:
        f.write("\nPatient {} exited, {} is free\n".format(patient.name, avl_doc.name))

    avl_doc.isfree = True
    if len(waiting_queue) > 0:
        thread = threading.Thread(
            target=assignment, args=(waiting_queue.pop(0), avl_doc, waiting_queue)
        )
        thread.start()
