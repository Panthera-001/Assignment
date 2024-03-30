# Create a new text file in write mode and write some content
with open("my_file.txt", "w") as file:
    file.write("Manchester United is the best club in England\n")
    file.write("12345\n")
    file.write("The season ends with Unied as number 1, Arsenal 12 and Chelsea relegated\n")

# Read the contents of the file and display them
print("Contents of my_file.txt:")
with open("my_file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Open the file in append mode and append three additional lines of text
with open("my_file.txt", "a") as file:
    file.write("This is the day\n")
    file.write("67890\n")
    file.write("When will it finally come to an end\n")

# Read the updated contents of the file and display them
print("\nUpdated contents of my_file.txt:")
with open("my_file.txt", "r") as file:
    for line in file:
        print(line.strip())
