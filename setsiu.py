# Program to perform different set operations as per user input

# Take input from user for set E
E_input = input("Enter elements of set E separated by spaces: ")
# Convert input string to set of integers
E = set(map(int, E_input.split()))

# Take input from user for set N
N_input = input("Enter elements of set N separated by spaces: ")
# Convert input string to set of integers
N = set(map(int, N_input.split()))

# Perform set operations
# set union
print("Union of E and N is", E | N)

# set intersection
print("Intersection of E and N is", E & N)

