# Counting the frequency of elements in a list
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}

for element in elements:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print(frequency)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
