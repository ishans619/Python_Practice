def my_func(rad):
    pi = 22/7
    area = pi*rad*rad
    print(f"area of the circle will be: {area} ")

n = 1
while(n>=1 and n<=10):
    rad = int(input(f"enter the radius of the {n} circle: "))
    my_func(rad)
    n = n + 1

print("ISHAN SHUKLA,21BCS7129")