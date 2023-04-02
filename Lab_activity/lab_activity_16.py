def last(n):
    return n[-1]


def sort(b):
    return sorted(b, key=last)


a = [(1, 3), (3, 2), (2, 1), (4, 4), (5, 0)]

print("original list:", a)
print("after sorting in increasing order by the last element in each tuple", sort(a))
print("ISHAN SHUKLA,21BCS7129")
