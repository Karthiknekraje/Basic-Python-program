# Remove a key-value pair using pop
removed_grade = student_grades.pop("Bob")
print("Removed Bob's grade:", removed_grade)
print("After removing Bob:", student_grades)

# Remove the last inserted key-value pair using popitem
last_item = student_grades.popitem()
print("Removed last item:", last_item)
print("After removing last item:", student_grades)
