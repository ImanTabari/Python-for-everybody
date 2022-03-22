'''
Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user
enters “done”. Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum
numbers after the loop completes.
'''
my_list = []
while(True):
    entry = input('Please enter your number, to exit entry insert "done": ')
    if entry == 'done':
        break
    else:
        my_list.append(int(entry))
print ('Maximum :', max(my_list), '\n','Minimum :', min(my_list))        