'''
Write a program to prompt for a file name, and then read through
the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
the line to extract the floating-point number on the line. Count these lines and
then compute the total of the spam confidence values from these lines. When you
reach the end of the file, print out the average spam confidence.
'''
while (True):
    fname = input('Please enter your file name: ')
    if fname == 'done': exit()
    else:
        try:
            fhand = open(fname)
            break
        except:
            print('Your file name %s does not exist. please try again. Or insert done to exit' %fname)

total_spam_line = 0
total_spam_value = 0
for line in fhand:
    if line.lower().startswith('x-dspam-confidence'):
    #if not line.lower().startswith('x-dspam-confidence'): continue    
        total_spam_line += 1
        total_spam_value += float(line[line.lstrip().find(' ')+1:])
#print('Avarage spam confidence is:' , total_spam_value/total_spam_line)
print('The avarage spam confidence in %s file is %g' %(fname, total_spam_value/total_spam_line))


