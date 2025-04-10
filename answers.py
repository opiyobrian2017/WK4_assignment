# Question 1

with open("answers.txt", "w") as file:
    file.write("My name is Brian Opiyo")
    file.write("\nI am the next tech dollar billionaire")

# Question 2

try:
    # open file with the name entered by the user
    with open(input("Enter the filename: "), "r") as file:
        data = file.read()
        print(data)
#display error if file is not found
except FileNotFoundError:
    print("File not found")

#display error if file is not readable  
except PermissionError:
    print("file cant be read")
