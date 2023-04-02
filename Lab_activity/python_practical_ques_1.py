def area(radius):
    pi = 22/7
    area = pi * radius * radius
    return area

def circumference(radius):
    pi = 22/7
    circumference = 2 * pi * radius
    return circumference

i = 0

while(i<5):
    radius = int(input("enter the radius: "))
    print(f"The area of the circle is: {area(radius)}")
    print(f"The circumference of the circle is: {circumference(radius)}")
    i = i + 1


