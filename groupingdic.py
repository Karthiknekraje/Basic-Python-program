# Grouping elements by a key
students = [
    {'name': 'John', 'grade': 'A'},
    {'name': 'Jane', 'grade': 'B'},
    {'name': 'Dave', 'grade': 'A'},
    {'name': 'Lucy', 'grade': 'C'}
]

grouped_by_grade = {}

for student in students:
    grade = student['grade']
    if grade not in grouped_by_grade:
        grouped_by_grade[grade] = []
    grouped_by_grade[grade].append(student['name'])

print(grouped_by_grade)
# Output: {'A': ['John', 'Dave'], 'B': ['Jane'], 'C': ['Lucy']}
