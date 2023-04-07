# This program will calculate the average of the three entered values.

value_1 = 0
value_2 = 0
value_3 = 0

print('*******************************************************************')
print('This program will calculate the average of the three entered values')
print('*******************************************************************\n')

value_1 = float(input('Please enter value 1: '))
value_2 = float(input('Please enter value 2: '))
value_3 = float(input('Please enter value 3: '))

average = (value_1 + value_2 + value_3) / 3

print(f'\nThe average of the three entered values is {average:.2f}')

input()
