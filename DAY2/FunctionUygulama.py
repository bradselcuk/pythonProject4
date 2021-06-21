# def yazdir(txt, adet):
#     print(txt * adet)
#
# yazdir("Bulent   ", 10)
#-------------------------
# def hesapla(number1,number2):
#     print((number1 * number2)-number2+number1)
#
# hesapla(20,49)
#-------------------------
def now():
    import datetime
    return datetime.datetime.now().year

def agecalCulation():
    return now() - 1881

agecalCulation()
sonuc = agecalCulation()
print(f"Ataturk is {sonuc} years old")

