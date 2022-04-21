class Patient:
    def __init__(self, id, name, age, problems, duration):
        if id == "none":
            self.id = self.generateId()
        else:
            self.id = id
        self.name = name
        self.age = age
        self.problems = []
        self.problems.insert(0, problems)
        self.duration = duration
        self.bills = []
        self.visits = []  # Durations
        self.visits.insert(0, duration)

    def generateId(self):
        id = self.name + str(self.age)
        return id

    def details(self):
        return {
            "name": self.name,
            "id": self.id,
            "age": self.age,
            "problem": self.problems,
            "visits": self.visits,
            "bills": self.bills,
        }
