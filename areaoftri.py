def triangle_area_coordinates(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

# Example usage
x1, y1 = 0, 0
x2, y2 = 4, 0
x3, y3 = 4, 3
area = triangle_area_coordinates(x1, y1, x2, y2, x3, y3)
print(f"The area of the triangle is: {area}")
