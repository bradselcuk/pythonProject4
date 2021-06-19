isimler =['Ada','Yigit','Hasan','Beril']
yaslar = [1998,2000,1998,1987]

isimler.append('Cenk')
isimler.insert(0,'Sena')
index = isimler.index('Yigit')
print(index)
isimler.remove("Yigit")

print(isimler)

sonuc = "Beril" in isimler
print(sonuc)

if "Beril" in isimler:
    print("yes")

isimler.reverse()
yaslar.reverse()

print(isimler)
print(yaslar)

s="IphoneX,IPhone XR"

sonuc=s.split(",")
print(sonuc)