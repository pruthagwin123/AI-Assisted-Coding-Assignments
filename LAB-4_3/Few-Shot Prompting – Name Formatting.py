#Write a Python function that accepts a full name and formats it as "Last, First".
#Examples:
#"John Smith" → "Smith, John"
#"Anita Rao" → "Rao, Anita"
def format_name(full_name):
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[-1] + ", " + parts[0]
    else:
        return "Invalid Name"
# Example usage:
name_input = input("Enter full name (First Last): ")
result = format_name(name_input)
print(result)
#generate remarks for Few-Shot Prompting – Name Formatting
# Remarks:
# This function takes a full name as input in the format "First Last" and splits it
#   into first and last names. It then returns a formatted string in the "Last, First" format.
# The example usage demonstrates how to use the function by prompting the user for a full name
#   and displaying the reformatted result.
