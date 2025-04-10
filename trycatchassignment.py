# Create the initial file named wk3answer.txt
initial_filename = "wk3answer.txt"
with open(initial_filename, "w") as file:
    file.write("This is the initial content of the file.\n")

# Program to read a file and write a modified version to a new file
def main():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ")

        # Attempt to open and read the file
        with open(filename, "r") as file:
            content = file.readlines()

        # Modify the content (example: add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read.")

if __name__ == "__main__":
    main()