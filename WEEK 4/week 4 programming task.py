# exercise.1

def int_checker(a):
    """This function takes in an integer as a parameter and returns True if the parameter is in the given range and returns False if it is not."""
    if a in range(0, 101):
        return print(True)
    else:
        return print(False)
entered_number = int(input("Enter a number: "))
int_checker(entered_number)

# exercise.2

def case_checker(entered_string):
    """This function takes in a string and counts the number of uppercase and lowercase letters in it."""
    for char in entered_string:
        print(char)


case_checker("AAAAsssss")

# exercise.3

def case_manager(name):
    """This function takes in a string as a parameter and changes the first character to uppercase and the rest to lowercase."""

    return name[0].upper() + name[1:].lower()


entered_name = input('Hello, What is your name? ')

print(f"Hello, {case_manager(entered_name)}. Good to meet you!")

# exercise.4

def char_remover(string):
    """This function takes in a string as a parameter and removes the last character of the string if its length is longer than 1."""

    if len(string) > 1:
        return print(f"String with the last letter removed: {string[:-1]}")
    else:
        return print("No changes")


entered_string = input("Enter a string: ")

char_remover(entered_string)

# exercise.5

def to_celsius(temp):
    """Converts the entered temperature in Fahrenheit to Celsius"""
    conv_temp = (temp - 32) * 5/9
    return print(f"Temperature in Celsius: {conv_temp}")


def to_fahrenheit(temp):
    """Converts the entered temperature in Celsius to Fahrenheit"""
    conv_temp = temp * 9/5 + 32
    return print(f"Temperature in Fahrenheit: {conv_temp}")


entered_temp = float(input('Enter your temperature: '))

to_celsius(entered_temp)
to_fahrenheit(entered_temp)

# exercise.6

def to_fahrenheit(temp):
    """Converts the entered temperature in Celsius to Fahrenheit"""
    conv_temp = float(temp[:-1])
    return print(f"{temp} converted to Fahrenheit is: {conv_temp * 9/5 + 32}F")


entered_temp = input("Enter your temperature: ")

to_fahrenheit(entered_temp)

# exercise.7

from statistics import mean


def read_temperatures():
    """
    Reads 6 temperatures from the user, calculates and displays the maximum, minimum,
    and mean of these temperatures.
    """
    temperatures = []
    for i in range(6):
        temp = float(input(f"Enter temperature {i+1}: "))
        temperatures.append(temp)

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = mean(temperatures)

    return max_temp, min_temp, mean_temp


max_temp, min_temp, mean_temp = read_temperatures()


print(f"The max temperature is: {max_temp},\nThe min temperature is: {
      min_temp},\nThe mean temperature is: {mean_temp}")

# exercise . 8

from statistics import mean


def read_temperatures():
    """
    Reads 6 temperatures from the user, calculates and displays the maximum, minimum,
    and mean of these temperatures.
    """
    temperatures = []
    i = 0
    end_input = False

    while end_input != True:
        entered_temp = input(f"Enter temperature {i+1}: ")
        i += 1

        if len(entered_temp) == 0:
            end_input = True
            break
        else:
            temp = float(entered_temp)
            temperatures.append(temp)

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = mean(temperatures)

    return max_temp, min_temp, mean_temp


max_temp, min_temp, mean_temp = read_temperatures()


print(f"The max temperature is: {max_temp},\nThe min temperature is: {
      min_temp},\nThe mean temperature is: {mean_temp}")