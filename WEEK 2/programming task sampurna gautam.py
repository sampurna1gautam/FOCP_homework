    # Question no.1

name = input("Hello, what is your name? ")
print("Hello " + name + ". Good to meet you!")


# Question no.2 

celsius = int(input("Enter the Temperature in Celsius:\n"))
fahrenheit = (1.8 * celsius) + 32
print(str(celsius) + " is equivalent to " + str(fahrenheit) + " Fahrenheit.")


# Question no.3 

num_std = 113
req_size = 22
groups = num_std // req_size
remaining_students = num_std % req_size
print("There will be " + str(groups) + " groups and " + str(remaining_students) + " leftovers.")


# Question no.4 
num_students = int(input("How many students? "))
num_sweets = int(input("how many sweets ? "))
sweets_per_student = num_sweets // num_students
remaining_sweets = num_sweets % num_students
print("Each student should receive " + str(sweets_per_student) + " sweets and " + str(remaining_sweets) + "will be leftovers.")
