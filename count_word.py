file_name = "names.txt"

f = open(file_name, "r")
content = f.read()
words = content.split()
f.close()

print(f"{file_name} me total {len(words)} words hain.")