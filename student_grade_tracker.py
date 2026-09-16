students = [
    ("Aman", [85, 78, 92]),
    ("Priya", [45, 52, 48]),
    ("Rohan", [70, 75, 80]),
    ("Sneha", [95, 88, 91]),
]

passing_marks = 50
report_card = {}
passed_students = set()

for name, marks in students:
    average = sum(marks) / len(marks) if len(marks) > 0 else 0
    status = "Pass" if average >= passing_marks else "Fail"
    
    if status == "Pass":
        passed_students.add(name)
        
    report_card[name] = {
        "marks": tuple(marks),
        "average": round(average, 2),
        "status": status,
        "grade": "A" if average >= 85 else ("B" if average >= 60 else "C")
    }

print("STUDENT REPORT CARDS:")
for name, data in report_card.items():
    print(name, ":", data)

print("\nPASSED STUDENTS SET:")
print(passed_students)