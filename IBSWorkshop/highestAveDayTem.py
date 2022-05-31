temperatures = [{'monday': 12,'wednesday': 13,'friday': 14},{'monday': 15,'friday': 12},{'tuesday': 10, 'thursday': 11,'saturday': 12},]
my_dic = dict()
count = 1
for elm in temperatures:
    for day in elm:
        if day not in  my_dic:
            my_dic[day] = (elm[day], count)
        else:
            my_dic[day] = (my_dic[day][0]+elm[day], count+1)    
#print (my_dic)
n_my_dic = sorted([(k,v) for k,v in my_dic.items()],key = lambda x: x[1][0]/x[1][1], reverse=True)           
print(n_my_dic[0][0])