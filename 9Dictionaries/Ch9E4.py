'''
Add code to the Ch9E3 program to figure out who has the most messages in the file.
After all the data has been read and the dictionary has been created, look through
the dictionary using a maximum loop (see Section 5.7.2) to find who has the most
messages and print how many messages the person has.
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
#-----------------------------------------------------------
'''
sorted_dic = sorted(email_dic.values(), reverse=True)
maximum = sorted_dic[0]
for keys in email_dic:
    if email_dic[keys] == maximum:
        print (keys , maximum)
'''
#------------------------------------------------------------
person , maximum = sorted([(values, key) for (key,values) in email_dic.items()], reverse=True)[0]
print (person,maximum)
