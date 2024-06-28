# Creating a dictionary
student = {
    'name': 'John Doe',
    'age': 21,
    'major': 'Computer Science'
}

# Accessing elements
print(student['name'])  # Output: John Doe

# Adding a new key-value pair
student['grade'] = 'A'

# Updating a value
student['age'] = 22

# Deleting a key-value pair
del student['major']

# Iterating over a dictionary
for key, value in student.items():
    print(f'{key}: {value}')
