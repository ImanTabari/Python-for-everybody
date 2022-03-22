'''
Revise a previous program as follows: Read and parse the “From”
lines and pull out the addresses from the line. Count the number of messages from
each person using a dictionary.
After all the data has been read, print the person with the most commits by creating
a list of (count, email) tuples from the dictionary. Then sort the list in reverse order
and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5

'''
# import string

while True:
    fname = input('Enter the file name: ')
    if fname == 'done':
        exit()
    try:
        fhand = open(fname)
        break
    except:
        print('the file name "%s" dose not exist. please try again or insert "done" to exit.' %fname)
email_dict = dict()
for line in fhand: 
    #line = line.translate(str.maketrans('','',string.punctuation)).split() #just to show how translate works. does not apply for this exercise
    line = line.split()
    if len(line) == 0 or line[0] != 'From': continue
    email_dict[line[1]] = email_dict.get(line[1],0)+1
       
# ------------------with list comprehenssion----------------------------------------
email , count = sorted([(value,key) for key,value in email_dict.items()],reverse=True)[0]
print(email,count)
'''
#----------------with append-----------------------------------------------------------  
email_list = []
for k,v in email_dict.items():
    email_list.append((v,k))

#email_list.sort()    
#print (email_list[-1])  
#----------------------------------------
#email_list.sort(reverse = True)
#print (email_list[0])
#----------------------------------
print(sorted(email_list,reverse=True)[0])
'''