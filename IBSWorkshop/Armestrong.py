'''
An Armstrong number is an n-digit number that is equal to the sum of the nth powers of its digits.
Let's demonstrate this for a 4-digit number: 1634 is a 4-digit number, raise each digit to the fourth power,
and add: 1^4 + 6^4 + 3^4 + 4^4 = 1634, so it is an Armstrong number.
For a 3-digit number: 153 is a 3-digit number, raise each digit to the third power, 
and add: 1^3 + 5^3 + 3^3 = 153, so it is an Armstrong number.

Write a simple program to check if a given number is an armstrong number. 
'''

def ArmestrongNum(num):
    digitlist = []
    Originalnum = num
    SumOfDigits = 0
    while num > 0:
        digitlist.append(num%10)
        num = num//10    
    for  item in digitlist:
        SumOfDigits += item**len(digitlist)
    if Originalnum == SumOfDigits:
        print(f'The number {Originalnum} is an Armestrong number.')
    else:
        print(f'The number {Originalnum} is not an Armestrong number.')
        
number = int(input('Enter the number: '))
ArmestrongNum(number)                   