# #value type => string,number
# # x=5
# # y=25
# #
# # x=y
# #
# # y=10
#
# # print(x,y)
#
# # referans type
#
# a = ["apple", "banana"]
# b = ["apple", "banana"]
#
# a = b
#
# b[0] = 'grape'
#
# print(a, b)


# list
import mimetypes

a=["apple","banana"]
print(type(a))

# tuple
b=["apple"],["banana"]
print(type(b))

# dictionary
c = {
    ' ':
        {
            'name': 'Cristiano Ronaldo', 'yearOfBirth': '1985', 'nationality': 'Portugal', 'current_team': 'Portugal', 'history': ['Juventus', 'Real Madrid', 'Portugal']
        },

        }
print(type(c))

# set
d = {"apple","banana","grappe"}
print(type(d))
