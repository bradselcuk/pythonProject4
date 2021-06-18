# if ile elif arasındaki fark.
# Eğer if deyimlerini art arda sıralayacak olursak,
# Python doğru olan bütün sonuçları listeleyecektir.
# Ama eğer if deyiminden sonra elif deyimini kullanırsak,
# Python doğru olan ilk sonucu listelemekle yetinecektir.
#
# a = 1
# b = 3
# if b > a:
#   print("1")
# if a < b:
#   print("2")
# else:
#   print("3")

# sonuc 1 ve 2 olur

a = 2
b = 33
if b > a:
  print("1")
elif a == b:
  print("2")
else:
  print("3")

# sonuc 1 olur