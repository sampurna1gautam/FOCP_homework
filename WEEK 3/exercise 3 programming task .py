# exercise.1
name = input("Enter your name: ")
if name:
    print(f"Hello, {name}!")
else:
    print("Hello, Stranger!")

# exercise .2
password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")

if password == confirm_password:
    print("Password Set")
else:
    print("Incorrect password")

# exercise .3
    
password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")
valid_password = valid_length = False

if len(password) >= 8 and len(password) <= 12:
    valid_length = True
    print('Valid length for the password')

    if password == confirm_password:
        valid_password = True

print("Valid password") if valid_length and valid_password else print(
    "Invalid password. Enter again")

# exercise .4
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
pass1 = input("Enter a new password (between 8-12 characters): ")
if 8 <= len(pass1) <= 12:
    if pass1 not in BAD_PASSWORDS:
        pass2 = input("Confirm your password: ")
        if pass1 == pass2:
            print("Password Successfully Set")
        else:
            print("Error: Passwords do not match. Please try again.")
    else:
        print("Error: Common password. Please choose a strong password.")
else:
    print("Error: Password must be between 8 and 12 characters long.")

# exercise .5
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")
valid_password = valid_length = good_password = False

if len(password) >= 8 and len(password) <= 12:
    valid_length = True

    if password not in BAD_PASSWORDS:
        good_password = True

    if password == confirm_password:
        valid_password = True

print("Valid password") if valid_length and valid_password and good_password else print(
    "Invalid password. Enter again")

# exercise .6
num = int(input("Enter a number: "))
for i in range(0, 13):
    print(f"{i} x {num} = {i*num}")

# exercise .7 
num = int(input("Enter a number: "))
if num in range(0, 13):
    for i in range(0, 13):
        print(f"{i} x {num} = {i*num}")
else:
    print("Please enter a number between range 0-12")

# exercise .8
entered_num = int(input("Enter a number: "))


if entered_num < 0:
    for i in range(12, 0, -1):
        print(f"{i} x {entered_num} = {i*entered_num}")
else:
    for i in range(0, 13):
        print(f"{i} x {entered_num} = {i*entered_num}")

