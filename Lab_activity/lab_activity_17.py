#
# a=["Red","Green","White","Black","Pink","Yellow"]
# del a[3:]
# print(a)
# del a[0]
# print(a)
# print("ISHAN SHUKLA,21BCS7129")

def area(radius):
    pi = 22/7
    area = pi*radius*radius
    return area

i = 0
while(i<5):
    radius = int(input("enter the radius for your circle: "))
    print(f"The area of your circle is {area(radius)}")
    i = i + 1

# i = 0
# avg = 0
# while(i<10):
#     number = int(input(f"Enter number {i}: "))
#     avg = avg + number
#     i = i + 1
#
# avg = avg/10
# print(f"The average of 10 numbers entered is {avg}.")

