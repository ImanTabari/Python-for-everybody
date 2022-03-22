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
    #line = ''.join(letter for letter in line.lower() if letter.isalnum()) # delete all spaces and punctuations(infact, delete everythings except numbers and alphabets- for just alphabet use .isalpha())
    #line = line.lower().translate(str.maketrans('','',string.punctuation)).translate(str.maketrans('','',string.whitespace)) # just by translate
    # it can be done by regular expressions too
    # with filter and lambda
    line = line.lower().translate(str.maketrans('','',string.punctuation)).translate(str.maketrans('','',string.digits)).replace(' ','').rstrip()
    for letter in line:
        letter_dict[letter] = letter_dict.get(letter,0)+1
letter_list = sorted([(v,k) for k,v in letter_dict.items()],reverse=True)        
for letter,count in letter_list:
    print (count,letter)       


           