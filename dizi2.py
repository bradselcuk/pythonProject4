sayilar = [1,5,8,9,5,3,45,5]
harfler = ['a','b','e','s','a','y']
heceler = ['abc','acc','avy','aaa']
sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = min(heceler)
sonuc = max(heceler)


#ekleme
sayilar.append(123)
sayilar.insert(3,99)
sayilar.insert(len(sayilar),1550)
sayilar.pop()
sayilar.pop(0)
sayilar.remove(123)
sonuc = sayilar
#siralama

harfler.sort()
sayilar.reverse()
sonuc = harfler

print(sayilar.count(5))
print(harfler.count('a'))
print(sayilar.index(45))

sonuc = sayilar
print(sonuc)