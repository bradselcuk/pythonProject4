# Class yapisi ve constructor olusturmak
class Personel:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.salary = salary
        self.email = f'{firstname.lower()}_{lastname.lower()}@company.com'

per_1 = Personel('John', 'Smith', 30000)
per_2 = Personel('Mary', 'Smith', 60000)

print(per_1.firstname)
print(per_1.lastname)
print(per_1.email)
print(per_1.salary)

print(per_2.firstname, per_2.lastname, per_2.email, per_2.salary)