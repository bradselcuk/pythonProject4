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
    def zam_oraninin_belirle(cls, oran):  # Class Methodu ile class manuple edilebillir, zam orani degistirilir
        cls.zamorani = oran

    @classmethod
    def from_string(cls, per_str): # Nesne yaratmanin method yolu
        firstname, lastname, salary = per_str.split('-')
        return cls(firstname, lastname, salary)

    @staticmethod  # sinif ve nesne argumani almaz
    def mesai_gunu(gun):
        if gun.weekday() == 5 or gun.weekday == 6:
            return 'HaftaSonu'
        else:
            return 'Hafta Ici'


import datetime
tarih = datetime.date(2020,3,27)
print(tarih.day)
print(Personel.mesai_gunu(tarih))


per_1 = Personel('John', 'Smith', 30000)  # Personel
per_2 = Personel('Mary', 'Smith', 60000)

per_str_1 = 'Sam-Winchester-40000'
per_str_2 = 'Dean-Winchester-60000'
per_str_3 = 'Bobby-Winchester-60000'

yeni_per_1 = Personel.from_string(per_str_2)
# print(yeni_per_1.email)
# print(yeni_per_1.salary)