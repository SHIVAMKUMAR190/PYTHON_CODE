marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("Total =", total)
print("Percentage =", percentage)
print("Highest Marks =", max(marks))
print("Lowest Marks =", min(marks))