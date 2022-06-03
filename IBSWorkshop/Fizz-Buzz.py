'''
Create a function called fizz_buzz_table that takes a positive integer (n) as an input, and returns the n x n multiplication table 
in a two dimensional array, where the “fizz-buzz” numbers are represented by their “fizz-buzz” string. 
A number is a “fizz-buzz” number if it’s a multiple of 3 or 5. If it’s a multiple of 3, it’s value should be Fizz. 
If it’s a multiple of 5, it’s value should be Buzz. If it’s a multiple of both 3 and 5, it’s value should be FizzBuzz.
'''

def FizzBuzz(num):
    FBMatrix = []
    for i in range(1, num + 1):
        Innerlist = []
        for j in range(1, num + 1):
            if i*j % 15 == 0:
                Innerlist.append('FizzBuzz')
            elif i*j % 5 == 0:
                Innerlist.append('Buzz')
            elif i*j % 3 == 0:
                Innerlist.append('Fizz')
            else:
                Innerlist.append(i*j) 
        FBMatrix.append(Innerlist)
    return FBMatrix

your_num = int(input('Please enter the number: '))
for item in FizzBuzz(your_num):
    print(item)        