import json

# File to store student data
filename = "students.json"

# Load student data from file
def load_students():
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # return empty list if file doesn't exist

# Save student data to file
def save_students(data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Calculate average score
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    total = sum(scores.values())
    return total / len(scores)

# Get grade based on average
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Add new student
def add_student(students):
    name = input("Enter student name: ")
    scores = {}

    while True:
        subject = input("Enter subject (or type 'done' to finish): ")
        if subject.lower() == "done":
            break
        score = float(input(f"Enter score for {subject}: "))
        scores[subject] = score

    average = calculate_average(scores)
    grade = get_grade(average)

    student = {
        "name": name,
        "scores": scores,
        "average": average,
        "grade": grade
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!\n")

# View all students
def view_students(students):
    if not students:
        print("No students found.\n")
        return
    for student in students:
        print("Name:", student["name"])
        print("Scores:", student["scores"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
        print("-" * 20)

# Main program
students = load_students()

while True:
    print("=== Student Report Card App ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")