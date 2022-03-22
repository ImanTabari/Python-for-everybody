'''
Write a program to read through the mail box data and when you
find line that starts with “From”, you will split the line into words using the split
function. We are interested in who sent the message, which is the second word on
the From line.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line and print out the second word for each From line,
then you will also count the number of From (not From:) lines and print out a
count at the end.
'''
while(True):
    fname = input('Please enter the file name: ')
    if fname == 'done':
        exit()
    try:    
        fhand = open(fname)
        break
    except:
        print ('your file name "%s" does not exist. please try again or insert "done" to exit.' %fname)
Fromline_count = 0
for line in fhand:
    if line.split() == [] or line.split()[0] != 'From' : continue
    else:    
        Fromline_count += 1
        print(line.split()[1]) 
print('The number of lines start with "From" equals to %d' %Fromline_count)                       