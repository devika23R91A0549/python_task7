# student_records.py

import json

# 1. Store student details using dictionary
student = {
    "id": 101,
    "name": "Devika",
    "age": 21,
    "course": "Python",
    "marks": 85
}

print("Original Student Record:")
print(student)

# 2. Access keys and values
print("\nAccessing Keys and Values:")
print("Keys:", student.keys())
print("Values:", student.values())

# 3. Update entries
student["marks"] = 90
student["grade"] = "A"
print("\nAfter Updating Record:")
print(student)

# 4. Delete an entry
del student["age"]
print("\nAfter Deleting 'age':")
print(student)

# 5. Loop through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"{key} : {value}")

# 6. Convert dictionary to JSON
student_json = json.dumps(student, indent=4)
print("\nDictionary converted to JSON:")
print(student_json)

# 7. Save JSON to file
with open("student.json", "w") as file:
    file.write(student_json)

print("\nStudent data saved to student.json")

# 8. Read JSON back into Python
with open("student.json", "r") as file:
    loaded_student = json.load(file)

# 9. Print clean formatted output
print("\nFormatted Student Record (Loaded from JSON):")
print("-------------------------------------------")
print(f"ID     : {loaded_student['id']}")
print(f"Name   : {loaded_student['name']}")
print(f"Course : {loaded_student['course']}")
print(f"Marks  : {loaded_student['marks']}")
print(f"Grade  : {loaded_student['grade']}")
