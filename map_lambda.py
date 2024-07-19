list_1 = [x for x in range(1,10)]
list_2 = list(map(lambda x:x*x,list_1))
for i in range(len(list_1)):
    print(f'{list_1[i]}^2 = {list_2[i]}')