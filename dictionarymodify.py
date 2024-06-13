# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Initial dictionary:", person)

# Adding an element
person["email"] = "alice@example.com"
print("After adding email:", person)

# Removing an element
del person["age"]
print("After deleting age:", person)

# Accessing elements
print("Name:", person["name"])
print("City:", person["city"])
