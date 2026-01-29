#Write a Python function that reads a .txt file and counts the number of lines.
# Examples:
# File content:
# Hello
# World
# → Output: 2 lines
# File content:
# Python
# AI
# Lab
# → Output: 3 lines
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return f"The number of lines in the file is: {len(lines)}"
    except FileNotFoundError:
        return "File not found. Please check the file path."
# Example usage:
file_path_input = input("Enter the path to the .txt file: ")
result = count_lines_in_file(file_path_input)
print(result)
#generate remarks for Few-Shot Prompting – File Handling (Line Count)
# Remarks:
# This function reads a specified .txt file and counts the number of lines it contains.
# It uses a try-except block to handle potential file not found errors gracefully.
# The function opens the file in read mode, reads all lines into a list, and returns the count of lines.
# The example usage demonstrates how to use the function by prompting the user for the file path
# and displaying the line count result. The provided examples illustrate the expected output for
# different file contents.

