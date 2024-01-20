# Exercise 1

print('Hello World!')

# Exercise 2

name = input('Enter your name- ')
print('Hello', name)

 #Exercise 3

temp = input('Enter temperature in Celsius- ')

conv_temp = float(temp) * 9/5 + 32

print('Entered temperature,', temp, 'C')
print('The temperature in Fahrenheit,', conv_temp, 'F')

# Exercise 4

matches = 609
batted = 1014
not_out = 162
runs_scored = 48426

batting_avg = runs_scored / (batted - not_out)

print('Player Name - Geoffrey Boycott')
print('Matches played -', matches)
print('Total times batted -', batted)
print('Total times not out -', not_out)
print('Total runs -', runs_scored)
print('Boycotts Batting Average -', round(batting_avg, 2))

# Exercise 5

# def sum(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + sum(arr[1:])


class_size = [113, 175, 12]
lab_group = 24

for student in class_size:
    complete_groups = student // lab_group
    remaining_students = student % lab_group

    print('Group size:', student)
    print('Total number of complete groups:', complete_groups)
    print('Remaining students:', remaining_students)


# total_students = sum(arr)
# complete_groups, remaining_students = divmod(total_students, lab_group)