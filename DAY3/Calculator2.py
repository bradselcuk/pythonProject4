print("----- C A L C U L A T O R -----")
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("--------------------------------")
a = int(input("Please Select Operation: "))
print("---------------------------------")

if a == 1:
    print(" A D D I T I O N ")
    print("+++++++++++++++++")
    num1 = int(input('Enter First Number: '))
    num2 = int(input('Enter second Number: '))
    def topla(num1,num2):
        print(f"Result: {num1+num2}")
    topla(num1,num2)
# --------------------------------------------
elif a == 2:
     print(" S U B T R A C T I O N ")
     print("_________________")
     num3 = int(input('Enter First Number: '))
     num4 = int(input('Enter second Number: '))
     def cikart(num3,num4):
         print(f"Result: {num3 - num4}")
     cikart(num3,num4)

elif a == 3:
     print(" M U L T I P L I C A T I O N ")
     print("*****************")
     num5 = int(input('Enter First Number: '))
     num6 = int(input('Enter second Number: '))
     def carp(num5, num6):
         print(f"Result: {num5 * num6}")
     carp(num5, num6)
elif a == 4:
     print("D I V I S I O N ")
     print("////////////////")
     num7 = int(input('Enter First Number: '))
     num8 = int(input('Enter second Number: '))
     def bol(num7, num8):
         print(f"Result: {num7 / num8}")
     bol(num7, num8)
