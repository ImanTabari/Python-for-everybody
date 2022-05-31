'''
Write a program that reads a file and prints the letters in decreasing
order of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different
languages and see how letter frequency varies between languages. Compare your
results with the tables at wikipedia.org/wiki/Letter_frequencies
'''
import string
while True:
    fname = input('Enter the file name: ')
    if fname == 'done':
        exit()
    try:
        fhand = open(fname)
        break
    except:
        print('the file name "%s" dose not exist. please try again or insert "done" to exit.' %fname)
letter_dict = dict()
for line in fhand:
    #line = ''.join(letter for letter in line.lower() if letter.isalnum()) # delete all spaces and punctuations(infact, delete everythings except numbers and alphabets- for having just alphabet use .isalpha())
    #line = line.lower().translate(str.maketrans('','',string.punctuation)).translate(str.maketrans('','',string.digits)).translate(str.maketrans('','',string.whitespace)) # just by translate
    # it can be done by regular expressions too
    # with filter and lambda
    line = line.lower().translate(str.maketrans('','',string.punctuation)).translate(str.maketrans('','',string.digits)).replace(' ','').replace('\t','').strip() # strip deletes everythings(tab,space,newline) from tail and head of string
                                                                                                                                                                  # we used .replace(' ','').replace('\t','') to remove space and tab in the middle of text                              
        #print(line)
    for letter in line:
        letter_dict[letter] = letter_dict.get(letter,0)+1

letter_list = sorted([(v,k) for k,v in letter_dict.items()],reverse=True)        
print(letter_list)
for count ,letter in letter_list:
    print (letter,count)       
most_frequent_letter = [(v,k) for k,v in letter_list if k == letter_list[0][0]]
if len(most_frequent_letter) > 1:
    print(f'This list: {most_frequent_letter} is your most frequent letters. You can pick one by choosing the order of letter.\n')
    letter = input('Please decide which letter you want to be printed by entering the order of it in the list: ')
    print(f'You made your decision. It is = {most_frequent_letter[int(letter)-1]}')
else: print(f'This list: {most_frequent_letter} is your most frequent letters.')
           