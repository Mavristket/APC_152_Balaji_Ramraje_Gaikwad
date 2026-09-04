source_file = input("Enter Python source file: ")
output_file = input("Enter output file name: ")

with open(source_file, "r") as source, open(output_file, "w") as output:
    for line in source:
        if not line.lstrip().startswith("#"):
            output.write(line)

print("Comments removed from the new file.")
