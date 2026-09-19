file_name = "names.txt"

f = open(file_name, "r")
lines = f.readlines()
total_lines = len(lines)
f.close()

print(f"{file_name} me total {total_lines} lines hain.")