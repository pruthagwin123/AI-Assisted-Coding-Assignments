#A) Zero-Shot Prompting – Vowel Count
#Write a Python function that accepts a string and returns the number of vowels in the string.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return f"The number of vowels in the given string is: {count}"
# Example usage:
string_input = input("Enter a string: ")
result = count_vowels(string_input)
print(result)
#generate remarks for Zero-Shot Prompting – Vowel Count
# Remarks:
# This function counts the number of vowels in a given string by iterating through each character
# and checking if it is present in the defined set of vowels (both uppercase and lowercase).
# It uses a generator expression to sum up the total count of vowels found in the input string.
# The function returns a formatted string indicating the total number of vowels.
# The example usage demonstrates how to use the function by prompting the user for a string
# and displaying the vowel count result.

#B) Few-Shot Prompting – Vowel Count
#Write a Python function that accepts a string and returns the number of vowels in the string.
#Examples:
#"Hello World" → 3
#"Python Programming" → 4
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return f"The number of vowels in the given string is: {count}"
# Example usage:
string_input = input("Enter a string: ")
result = count_vowels(string_input)
print(result)
#generate remarks for Few-Shot Prompting – Vowel Count
# Remarks:
# This function counts the number of vowels in a given string by iterating through each character
# and checking if it is present in the defined set of vowels (both uppercase and lowercase).
# It uses a generator expression to sum up the total count of vowels found in the input string.
# The function returns a formatted string indicating the total number of vowels.
# The example usage demonstrates how to use the function by prompting the user for a string
# and displaying the vowel count result. The provided examples illustrate the expected output for
# different input strings.


#Compare both outputs based on:
#  Accuracy
#  Readability
#  Logical clarity
# Comparison of Zero-Shot vs Few-Shot Prompting – Vowel Count
# 1. Accuracy:
# Both implementations accurately count the number of vowels in the input string. They use the same logic
# to identify vowels and return the correct count. Therefore, there is no difference in accuracy between
# the two approaches.
# 2. Readability:
# Both implementations are equally readable. They use clear variable names and a straightforward approach
# to count vowels. The use of a generator expression makes the code concise and easy to understand in both cases.
# 3. Logical Clarity:
# Both implementations exhibit logical clarity by clearly defining the purpose of the function and the steps
# taken to achieve that purpose. The logic for counting vowels is straightforward and easy to follow in both implementations.
# Overall, there is no significant difference between the Zero-Shot and Few-Shot Prompting
# implementations in terms of accuracy, readability, or logical clarity. Both approaches effectively
# achieve the same result using similar methods.

