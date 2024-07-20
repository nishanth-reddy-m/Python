def lab1(table):
    max = 0
    average = 0
    date = ''
    for day in range(1,11):
        index = f'Jan {day}'
        average += table[index]
        if day == 7:
            print(f'Average of first week: {(average/7):.2f}')
        if table[index] > max:
            date = index
            max = table[index]
    print('The maximum temperature was %.2f'%max,'on',date)
def lab2(table):
    one = 'Jan 9'
    two = 'Jan 4'
    print(f'Temperature on {one}: {table[one]}')
    print(f'Temperature on {two}: {table[two]}')
def csv():
    table = {}
    with open('nyc_weather.csv','rt') as file:
        file.readline()
        for line in file:
            data = line.split(',')
            table[data[0]] = float(data[1])
    return table
def poem():
    data = {}
    with open('poem.txt','rt') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in data:
                    data[word] += 1
                else:
                    data[word] = 1
    return data

table = csv()
lab1(table)
lab2(table)
data = poem()
for item in data:
    print(f'{item}:{data[item]}')