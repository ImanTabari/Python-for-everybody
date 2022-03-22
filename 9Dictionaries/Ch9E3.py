'''
Write a program to read through a mail log, build a histogram using
a dictionary to count how many messages have come from each email address,
and print the dictionary.
'''
while True:
    fname = input('Please enter your file name: ')
    if fname == 'done':
        exit()
    try:
        fhand = open(fname)
        break
    except:
        print('Your file name "%s" dose not exist. please try again or insert "done" to exit.' %fname)
email_dic = dict()
for line in fhand:
    if len(line.split()) == 0 or line.split()[0] != 'From': continue
    email_dic[line.split()[1]] = email_dic.get((line.split()[1]),0) +1 
print (email_dic)            