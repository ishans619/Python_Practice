def square(side):
    perimeter = 4*side
    return perimeter

def rectangle(length,bredth):
    perimeter = 2*(length+bredth)
    return perimeter

def triangle(a,b,c):
    perimeter = a+b+c
    return perimeter

side = int(input("enter the side for the square: "))
print(f"The perimeter of the square is {square(side)}")

lenght = int(input("enter the length of the rectangle: "))
bredth = int(input("enter the bredth of the rectangle: "))
print(f"The perimeter of the rectangle is {rectangle(lenght,bredth)}")

a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the traingle: "))
c = int(input("Enter the third side of the triangle: "))
print(f"The perimeter of triangle is {triangle(a,b,c)}")
