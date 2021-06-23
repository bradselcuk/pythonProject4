def selamlama(isim,mesaj):

    print(f'{mesaj}  {isim}')
\
selamlama("Bulent", "Gunaydin")


# def usAlma(taban,us):
#     return taban**us
# sonuc = usAlma(3,2)
# print(sonuc)

#ikinci yol
# def usAlma(taban,us=2):
#     return taban**us
# sonuc = usAlma(3)
# print(sonuc)

def toplam (a,b):
    return a+b

def islem(a,b,fn):
    return fn(a,b)

sonuc = islem(1,3,toplam)
print(sonuc)