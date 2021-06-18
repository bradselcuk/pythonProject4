ogrenciA = ["Yigit","Turan",2010,[60,80,90]]
ogrenciB = ["Sena","Turan",2011,[50,80,90]]
ogrenciC = ["Ahmet","Turan",2015,[60,60,90]]

ogrenciler = [ogrenciA, ogrenciB, ogrenciC]

for ogrenci in ogrenciler:
    print(ogrenci[3])


#print(ogrenci)

for ogrenci in ogrenciler:
    print(f"{ogrenci[0]} {ogrenci[1]} {ogrenci[3][0]}")