def find_rainiest(file):
    try:
        cityfile = open(file)
    except IOError:
        print(('File is not found!'))
        exit()
    city_sumofrain = {}
    for line in cityfile:
        line.strip()
        spliter = ';'
        line = line.split(spliter)
        city_sumofrain[line[1]] = city_sumofrain.get(line[1],0) + int(line[2])      
    cities = [(v,k) for k,v in city_sumofrain.items()]
    cities.sort(reverse=True)
    count = 0
    for i in range(0,len(cities)):
        if  cities[i][0] == cities[0][0]:
            count += 1
    if count > 1:
        choose = int(input(f'you have "{count}" cities with the same amount of rainfall,\n"choose one by entering a number": '))
        print(cities[choose-1][1])
    else: print(cities[0][1])            


weather = input('Enter your file name: ')
answer = find_rainiest(weather)
   
