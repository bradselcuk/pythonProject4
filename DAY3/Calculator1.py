a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))

def topla(num1,num2):
    return num1+num2

sonuc1 = topla(a,b)
print(sonuc1)

c=int(input("Enter first Number: "))
d=int(input("Enter second Number: "))

def multipl(num2,num3):
    return num2*num3
sonuc2 = multipl(c,d)
print(sonuc2)

def lastPrice():
    return sonuc1/sonuc2

lastPrice()
sonuc3= lastPrice()
print('+++++++++++++++++++++')
print(f'result: {sonuc3}')