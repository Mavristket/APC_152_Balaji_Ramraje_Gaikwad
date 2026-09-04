source_file = input("Enter source file name: ")
output_file = input("Enter output file name: ")

with open(source_file, "r") as source:
    text = source.read().upper()

with open(output_file, "w") as output:
    output.write(text)

print("Uppercase file created.")
