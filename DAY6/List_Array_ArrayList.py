# cars = ["Ford", "Volvo", "BMW"]
# count=0
# for x in cars:
#     count= count+1
#     print(f" line:  {count} ===> {x}")
#
# a = input("Enter new car: ")
# cars = {"Ford", "Volvo", "BMW"}
# cars.add(a)
#
#
# count=0
# for x in cars:
#     count= count+1
#     print(f" line:  {count} ===> {x}")
#


a = input("Enter new car: ")
cars = ["Ford", "Volvo", "BMW"]
cars.append(a)
cars.sort()

count=0
for x in cars:
    count= count+1
    print(f" line:  {count} ===> {x}")

