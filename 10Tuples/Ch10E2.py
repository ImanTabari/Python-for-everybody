'''
This program counts the distribution of the hour of the day for
each of the messages. You can pull the hour from the “From” line by finding the
time string and then splitting that string into parts using the colon character. Once
you have accumulated the counts for each hour, print out the counts, one per line,
sorted by hour as shown below.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
'''
while True:
    fname = input('Enter the file name: ')
    if fname == 'done':
        exit()
    try:
        fhand = open(fname)
        break
    except:
        print('the file name "%s" dose not exist. please try again or insert "done" to exit.' %fname)
hour_dict = dict()
for line in fhand:
    line = line.split()
    if len(line) ==0 or line[0] != 'From': continue
    hour_dict[line[5].split(':')[0]] = hour_dict.get(line[5].split(':')[0],0)+1
for hour,count in sorted(hour_dict.items()):
    print(hour,count)

