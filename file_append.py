file_name = "names.txt"

f = open(file_name, "a")
f.write("Rohan\n")
f.write("Amit\n")
f.close()

print(f"Data {file_name} me append ho gaya.")