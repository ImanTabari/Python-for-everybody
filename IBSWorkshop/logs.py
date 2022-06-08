# Read all data from 'log.txt'
# Each line represents a log message from a web server
# Write a function that returns an array with the unique IP adresses
# Write a function that returns the GET / POST request ratio
def UniqueIPAddress(filename):
    try:
        fhand = open(filename)
    except IOError:
        print (f'The file name "{filename}" dose not exist.')
        exit()
    log_dict = {}
    for line in fhand:
        line = line.strip().split()
        if len(line) == 0: continue
        else:
            log_dict[line[5]] = log_dict.get(line[5],0) + 1
    return log_dict

def GetPostRatio(filename):
    try:
        fhand = open(filename)
    except IOError:
        print (f'The file name "{filename}" dose not exist.')
        exit()
    get_post_dict = {}
    for line in fhand:
        line = line.strip().split()
        if len(line) == 0: continue
        else:
            get_post_dict[line[6]] = get_post_dict.get(line[6],0) + 1
    get_post_ratio = get_post_dict['GET']/get_post_dict['POST']
    return get_post_ratio

fname = input('Enter the log file name: ')

my_dict = UniqueIPAddress(fname)

for IPAddress in my_dict:
    print(IPAddress)

print (len(my_dict))

print(GetPostRatio(fname))        


            
