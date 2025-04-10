# Question 1

with open("answers.txt", "w") as file:
    file.write("My name is Brian Opiyo")
    file.write("\nI am the next tech dollar billionaire")

# Question 2

try:
    with open(input("Enter the filename: "), "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found")