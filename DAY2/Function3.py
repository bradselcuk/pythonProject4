# def toplam():
#     return(f'toplam: {10+20}')
#
# # toplam()
# # print(toplam)
# a = toplam()
# print(a)

# def toplam():
#     return 10+20
# sonuc = toplam()+50
#
# print(sonuc)


# def yasHesapla():
#     return 2021-1967
# sonuc = yasHesapla()
# print(sonuc)


def simdi():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return simdi() - 1967

yasHesapla()
sonuc = yasHesapla()
print(sonuc)


def selamla():


