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
elif a == 2:
     print(" S U B T R A C T I O N ")
     print("_________________")
elif a == 3:
     print(" M U L T I P L I C A T I O N ")
     print("*****************")
elif a == 4:
     print("D I V I S I O N ")
     print("////////////////")
else:
    print("Application has been ended")
