class Personel:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.salary = salary
        self.email = f'{firstname.lower()}_{lastname.lower()}@company.com'
    def full_name(self):
        return f'{self.firstname} {self.lastname}'
    def zamuygula(self):
        self.salary = int(self.salary * 1.05)


per_1 = Personel('John', 'Smith', 30000)
per_2 = Personel('Mary', 'Smith', 60000)
per_2 = Personel('Test','User', 1000)


print(per_1.salary)
per_1.zamuygula()
print(per_1.salary)