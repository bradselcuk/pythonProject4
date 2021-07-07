class Personel:
    zamorani = 1.05
    personel_sayisi = 0

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.salary = salary
        self.email = f'{firstname.lower()}_{lastname.lower()}@company.com'

        Personel.personel_sayisi += 1

    def full_name(self):
        return f'{self.firstname} {self.lastname}'
    def zamuygula(self):
        self.salary = int(self.salary * self.zamorani) #Self = Personel

print(Personel.personel_sayisi) # Personel yaratilmadan once
per_1 = Personel('John', 'Smith', 30000)
per_2 = Personel('Mary', 'Smith', 60000)


# print(per_1.salary)
# per_1.zamuygula()
# print(per_1.salary)
# print(per_1.zamorani)
# print(Personel.zamorani) # Once Sinif tan yaratilan nesneye bakar bulamaz ise nesnenin yaratildigi sinifa bakar degiskeni bulur
# print(per_1.zamorani)
#
# print(per_2.salary)
# print(per_2.zamorani)
# per_2.zamuygula()
# print(per_2.salary)
# print("-----------------")
#
# Personel.zamorani = 2 # zam orani guncellendi
# print(per_1.zamorani)
# per_2.zamuygula()
# print(per_2.salary)
# print("______________________")
#
# per_2.zamorani = 5 # sadece personel 2 in zam orani degisti
# print(per_1.zamorani)
# print(per_2.zamorani)

print(Personel.personel_sayisi) #Personel yaratildiktan sonra

