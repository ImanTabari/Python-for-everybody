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
fname = input('Please enter the file name: ')
try:
    fhand = open(fname)
except:
    print('your file name %s dose not exist, please try agin.' %fname)
    exit()
for line in fhand:
   print(line.rstrip().upper())

