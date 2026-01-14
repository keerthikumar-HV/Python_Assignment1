# Program to write, append, and read data from a file

# Take user input and write to file
text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.\n")

# Take additional input and append to file
append_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.\n")

# Read and display final content
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
