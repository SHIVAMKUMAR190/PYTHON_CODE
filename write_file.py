file_name = "names.txt"

name = input("Apna naam enter karein: ")

f = open(file_name, "w")
f.write(name + "\n")
f.close()

print(f"{file_name} me naam save ho gaya.")