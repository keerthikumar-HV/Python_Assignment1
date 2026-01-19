
# Student Marks Dictionary Program (Case-Insensitive)

# Step 1: Create the dictionary (keys in lowercase)
students_marks = {
    "alice": 85,
    "bob": 78,
    "charlie": 92,
    "david": 88
}

# Step 2: Ask user for student name
name = input("Enter the student's name: ").strip().lower()

# Step 3 & 4: Retrieve and display marks or show message
if name in students_marks:
    # Capitalize name for display
    print(f"{name.capitalize()}'s marks: {students_marks[name]}")
else:
    print("Student not found.")
