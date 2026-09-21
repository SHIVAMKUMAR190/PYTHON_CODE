import os

target_file = "notes.txt"

with open(target_file, "w") as f:
    f.write("First line of the text.\nSecond line with some extra words.\n")

with open(target_file, "r") as f:
    lines = f.readlines()

total_lines = len(lines)
total_words = sum(len(line.split()) for line in lines)
file_size = os.path.getsize(target_file)

print(f"Report for {target_file}:")
print(f"Lines: {total_lines}")
print(f"Words: {total_words}")
print(f"Size: {file_size} bytes")