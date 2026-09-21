file_name = "config.txt"

with open(file_name, "w") as f:
    f.write("environment = staging\ndebug = true\n")

with open(file_name, "r") as f:
    content = f.read()

updated_content = content.replace("staging", "production")

with open(file_name, "w") as f:
    f.write(updated_content)

print(f"Updated content written to {file_name}")