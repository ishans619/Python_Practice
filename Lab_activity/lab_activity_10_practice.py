# def my_func(s):
#     str = ""
#     for item in s:
#         str = item + str
#     return str
#
# s = input("enter the string you want to get reverse of: ")
#
# print(f"The original string is: {s}")
# print(f"reversed string is: {my_func(s)} ")

str = input("enter the string: ")
print(tuple(reversed(str)))
