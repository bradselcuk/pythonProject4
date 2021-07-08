class Personel:
    personel_sayisi = 0
    zamorani = 1.05

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.salary = salary
        self.email = f'{firstname.lower()}_{lastname.lower()}@company.com'

        Personel.personel_sayisi += 1

    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    def zamuygula(self):
        self.salary = int(self.salary * self.zamorani)  # Self = Personel
    @classmethod
    def zam_oraninin_belirle(cls, oran): # Class Methodu ile class manuple edilebillir, zam orani degistirilir
        cls.zamorani = oran

per_1 = Personel('John', 'Smith', 30000)  # Personel
per_2 = Personel('Mary', 'Smith', 60000)

Personel.zam_oraninin_belirle(1.1)
print(Personel.zamorani)
print(per_1.zamorani) # Tum nesnelerin zam orani degisti
