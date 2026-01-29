#Write a Python function to convert centimeters to inches.
#Example:
# Input: 10 cm → Output: 3.94 inches

def cm_to_inches(cm):
    inches = cm / 2.54
    return f"{cm} cm is equal to {inches:.2f} inches."

# Example usage:
cm_input = float(input("Enter length in centimeters: "))
result = cm_to_inches(cm_input)
print(result)

#generate remarks for One-Shot Prompting – Centimeters to Inches Conversion

# Remarks:
# This function converts a given length from centimeters to inches using the conversion factor of 1 inch = 2.54 cm.
# It takes a floating-point number as input representing the length in centimeters and returns a formatted string
# indicating the equivalent length in inches rounded to two decimal places. The example usage demonstrates how to
# use the function by prompting the user for input and displaying the result.