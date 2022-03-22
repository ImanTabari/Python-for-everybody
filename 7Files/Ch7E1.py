'''
Write a program to read through a file and print the contents of the
file (line by line) all in upper case. Executing the program will look as follows:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
7.11. Exercises 89
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
'''
#import os
#print(os.getcwd())
while(True):
    fname = input('Please enter the file name: ')
    if fname == 'done': exit()
    else:
        try:
            fhand = open(fname)
            break
        except:
            print('your file name %s dose not exist, please try agin. Or insert done to exit.' %fname)
for line in fhand:
   print(line.rstrip().upper())

