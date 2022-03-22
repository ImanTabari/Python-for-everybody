'''
This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e., the
whole email address). At the end of the program, print out the contents of your
dictionary.
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
domain_dic = dict()
for line in fhand:
    if len(line.split()) == 0 or line.split()[0] != 'From': continue
    domain_dic[line.split()[1].split('@')[1]] = domain_dic.get(line.split()[1].split('@')[1],0)+1
print (domain_dic)            