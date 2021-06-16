msg = "Benim adim Bulent Selcuk, ben bir IT Uzmaniyim"


sonuc = msg.split()
print(sonuc)

print(sonuc[2])

sonuc = "-".join(sonuc)

index = msg.index('Bulent')
print(index)

sonuc = msg.startswith('B')
print(sonuc)
