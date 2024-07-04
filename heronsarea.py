import math

def triangle_area_heron(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Example usage
a = 7
b = 10
c = 5
area = triangle_area_heron(a, b, c)
print(f"The area of the triangle is: {area}")
