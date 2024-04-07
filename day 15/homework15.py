# def print_initials(full_name):
#     names = full_name.split()
#     if len(names) >= 2:
#         first_initial = names[0][0]
#         last_initial = names[-1][0]
#         print("Initials:", first_initial + '.' + last_initial)
#     else:
#         print("Invalid input. Please provide both first and last names.")

# # Example usage:
# full_name = "David Tezelashvili"

# print_initials(full_name)








# def calculate_arithmetic_mean(lst):
#     if len(lst) == 0:
#         print("Empty list!")
#         return
    
#     total_sum = 0
#     for num in lst:
#         total_sum += num

#     mean = total_sum / len(lst)
#     print("Arithmetic mean:", mean)

# # Example usage:
# numbers_list = [1, 2, 3, 4, 5]

# calculate_arithmetic_mean(numbers_list)








# def is_palindrome(word):
#     # Convert the word to lowercase for case-insensitive comparison
#     word = word.lower()
#     # Remove any spaces in the word
#     word = word.replace(" ", "")
#     # Check if the word is equal to its reverse
#     return word == word[::-1]

# # Example usage:
# word = "level"
# print(word, "is palindrome:", is_palindrome(word))

# word = "hello"
# print(word, "is palindrome:", is_palindrome(word))








# def remove_spaces(string):
#     # Remove spaces from the string
#     string_without_spaces = string.replace(" ", "")
#     # Print the modified string
#     print("Modified string:", string_without_spaces)

# # Example usage:
# input_string = "Goal-Oriented Academy"
# remove_spaces(input_string)







# def calculate_sum_of_positive_and_negative_numbers(numbers):
#     sum_positive = 0
#     sum_negative = 0

#     for num in numbers:
#         if num > 0:
#             sum_positive += num
#         elif num < 0:
#             sum_negative += num

#     print("Sum of positive numbers:", sum_positive)
#     print("Sum of negative numbers:", sum_negative)

# # Example usage:
# numbers_list = [1, -2, 3, -4, 5, -6]

# calculate_sum_of_positive_and_negative_numbers(numbers_list)
