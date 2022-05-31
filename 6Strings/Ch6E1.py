'''Write a while loop that starts at the last character in the string and
works its way backwards to the first character in the string.
'''

word = input('Please Enter a word: ')

#whith while loop
count = 1
while(count<=len(word)):
    #print (word[-count])  # each character is printed in a new line 
    print (word[-count], end='') #print in one line
    count +=1

# whith for loop
rev_word = '' # rev_word has to be defined befor using it in because python evaluate the right side in updating variables.                         
for index in range(len(word)):
    rev_word = word[index] + rev_word
print ('\n', rev_word, sep='') # \n is to print the output of this solution in new line after the out put of first one   
                               # after \n python puts space to print the second element in print function. so sep='' is to eleminate this space
rev_word = ''                          
for char in word:
    rev_word = char + rev_word
print ( rev_word)                               