string = "Hello, world!"
count = sum(1 for char in string if char.isalpha())
print(f"The total number of alphabetic characters is: {count}")
