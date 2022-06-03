'''
Write a function that can read and parse a file. It should take the name of the file as an input and return the most common word of 
the file (case insensitively). If multiple words are found as the most common you can decide which one to return. You can assume that:
the file contains multiple lines
the words are separated by spaces only
there can be , and . characters in the sentences
The function should handle possible exceptions by printing messages to the standard output.
'''
import string

def MostCommonWord(fname):
    try:
        fhand = open(fname)
    except IOError:
        print(('Your file does not exist.'))
        exit()
    word_dict = {}
    MCWordList = []
    for line in fhand:
        line = line.lower().translate(str.maketrans('','',string.punctuation )).translate(str.maketrans('','',string.digits)).split()
        if len(line) == 0: continue
        else:
            for word in line:
                word_dict[word] = word_dict.get(word, 0) + 1
    word_list = word_dict.items()
    word_list = sorted(word_list, key = lambda x: x[1], reverse = True)

    for item in word_list:
        if item[1] == word_list[0][1]:
            MCWordList.append(item[0])
    return MCWordList



fname = input('Please enter the file name: ')
words = MostCommonWord(fname)
if len(words) == 1:
    print(*words)
else:
    selectword = int(input(f'there are {len(words)} words with the same occurance:{words}. Enter its index to choose: '))
    print(words[selectword])    