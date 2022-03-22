'''
Write a program that categorizes each mail message by which day
of the week the commit was done. To do this look for lines that start with “From”,
then look for the third word and keep a running count of each of the days of the
week. At the end of the program print out the contents of your dictionary (order
does not matter)
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
days_dic = {}
for line in fhand:
    if len(line.split()) == 0 or line.split()[0] != 'From': continue
    days_dic[line.split()[2]] = days_dic.get(line.split()[2],0) + 1
print (days_dic)
for key in days_dic:
    print (key, days_dic[key])                    
