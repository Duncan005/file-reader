# File Read & Write with Error Handling
try:
    # Prompt user for input file
    input_file = input("Enter the name of the file to read: ")

    # Open and read the content of the file
    with open(input_file, "r") as file:
        content = file.readlines()

    # Modify the content (e.g., add line numbers)
    modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]

    # Write the modified content to a new file
    output_file = "modified_" + input_file
    with open(output_file, "w") as file:
        file.writelines(modified_content)

    print(f"Modified content has been written to {output_file}")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
