'''
Write a program to open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is not in the
list, add it to the list.
'''
while(True):
    fname = input('Please enter your file name: ')
    if fname == 'done':
        exit()
    try:
        fhand = open(fname)
        break
    except:
        print ('Your file name does not exist. Please try again or insert "done" to exit.')
word_list = []
for line in fhand:
    if line.split() == []: continue
    else:
        for word in line.split():
            if not word in word_list:
                word_list.append(word.lower())
print(sorted(word_list))                

