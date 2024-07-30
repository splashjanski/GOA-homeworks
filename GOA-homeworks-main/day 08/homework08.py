# Getting input from the user
name = input("Enter your name: ")
password = input("Enter your password: ")
repeat_password = input("Repeat your password: ")

# Checking if the passwords match
if password == repeat_password:
    print("You have successfully registered")
else:
    print("The passwords do not match. Please try again.")
