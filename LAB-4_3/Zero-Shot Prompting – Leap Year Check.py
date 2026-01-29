#Write a Python function that accepts a year as input and checks whetherthe given year is a leap year. 
# The function should return an appropriate result.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year."
    else:
        return f"{year} is not a leap year."
    
# Example usage:
year_input = int(input("Enter a year: "))
result = is_leap_year(year_input)
print(result)

#generate remarks for Zero-Shot Prompting – Leap Year Check

# Remarks:
# This function accurately determines whether a given year is a leap year based on the established rules:
# 1. A year is a leap year if it is divisible by 4.
# 2. However, if the year is divisible by 100, it is not a
#    leap year, unless it is also divisible by 400.
# 3. The function takes an integer input representing the year and returns a string indicating whether it is a
#    leap year or not. The example usage demonstrates how to use the function by prompting the user for input 
#    and displaying the result.



