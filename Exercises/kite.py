class employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def giveRaise(self, salary):
        self.salary = salary


class developer(employee):

    def __init__(self, firstname, lastname, salary, prog_lan):
        super().__init__(firstname, lastname, salary)
        self.prog_langs = prog_lan

    def addLan(self, lang):
        self.prog_langs += [lang]


employee1 = employee("john", "smith", 8000)

print(employee1.salary)

employee1.giveRaise(1000)

print(employee1.salary)


dev1 = developer("joe", "wick", 7000, ["Python", "C++"])

print(dev1.salary)

dev1.addLan("Java")

print(dev1.prog_langs)
