csv_file = "students.csv"

records = [
    ("Shivam", 101, 85),
    ("Aman", 102, 90),
    ("Rohan", 103, 78)
]

with open(csv_file, "w") as f:
    f.write("Name,Roll,Marks\n")
    for name, roll, marks in records:
        f.write(f"{name},{roll},{marks}\n")

print(f"Data exported successfully to {csv_file}")