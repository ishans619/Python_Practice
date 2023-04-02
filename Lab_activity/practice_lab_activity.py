# def armstrong(number):
#     sum = 0
#     temp = number
#
#     while(temp!=0):
#         digit = temp % 10
#         sum = sum + digit ** 3
#         temp //= 10
#     return sum
#
# number = int(input("enter the number to be checked for armstrong: "))
# a = armstrong(number)
# if(a==number):
#     print("armstorng")
# else:
#     print("not an armstrong")
#
#


def add_string(str1):
    length = len(str1)

    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'

    return str1


print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))