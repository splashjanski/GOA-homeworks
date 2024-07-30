# Check if the number entered by the user is exactly divisible by 2 and 4
def check_divisibility(num):
    if num % 2 == 0 and num % 4 == 0:
        return True
    else:
        return False

# Example 1: Greater than (>)
print(5 > 3)  # True
print(2 > 4)  # False

# Example 2: Less than (<)
print(5 < 3)  # False
print(2 < 4)  # True

# Example 3: Greater than or equal to (>=)
print(5 >= 3)  # True
print(4 >= 4)  # True

# Example 4: Less than or equal to (<=)
print(5 <= 3)  # False
print(4 <= 4)  # True

# Example 5: Equal to (==)
print(5 == 5)  # True
print(4 == 5)  # False

# Example 6: Not equal to (!=)
print(5 != 5)  # False
print(4 != 5)  # True

# Example 7: Greater than (>) with variables
a = 5
b = 3
print(a > b)  # True

# Example 8: Less than (<) with variables
a = 5
b = 3
print(a < b)  # False

# Example 9: Greater than or equal to (>=) with variables
a = 5
b = 3
print(a >= b)  # True

# Example 10: Less than or equal to (<=) with variables
a = 5
b = 3
print(a <= b)  # False

# Test the divisibility function
num = int(input("Enter a number: "))
if check_divisibility(num):
    print(num, "is divisible by both 2 and 4")
else:
    print(num, "is not divisible by both 2 and 4")
