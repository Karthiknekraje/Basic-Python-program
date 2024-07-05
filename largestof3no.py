def find_largest(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

# Example usage
a = 10
b = 14
c = 12
print(f"The largest number among {a}, {b}, and {c} is: {find_largest(a, b, c)}")
