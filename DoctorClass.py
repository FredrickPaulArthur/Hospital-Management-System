from random import randint


class Doctor:
    def __init__(self, name, fee):  # , time):
        self.name = name
        self.fee = fee
        self.isfree = True

    def __str__(self):
        return "{}\t {}\t {}\t".format(self.name, self.fee, self.time)
