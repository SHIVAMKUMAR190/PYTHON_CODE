file_name = "names.txt"

f = open(file_name, "r")
for line in f:
    print(line.strip())
f.close()
