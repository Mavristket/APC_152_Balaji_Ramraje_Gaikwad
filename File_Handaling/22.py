first_file = input("Enter first file name: ")
second_file = input("Enter second file name: ")
output_file = input("Enter output file name: ")

with open(first_file, "r") as first, open(second_file, "r") as second:
    combined_text = first.read() + second.read()

with open(output_file, "w") as output:
    output.write(combined_text)

print("The files were combined successfully.")
