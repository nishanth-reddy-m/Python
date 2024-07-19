from os import strerror
dictionary = {}
try:
    n = input('Enter the txt file name: ')
    stream1 = open(f'{n}.txt','rt')
    file = stream1.read()
    for char in file:
        if ord(char.lower()) in range(ord('a'),ord('z')+1):
            if char.lower() in dictionary:
                dictionary[char.lower()] += 1
            else:
                dictionary[char.lower()] = 1
    stream1.close()
    stream2 = open(f'{n}.hist','wt')
    for key in (sorted(dictionary.keys(),key=lambda x: dictionary[x],reverse=True)):
        data = f'{key} -> {dictionary[key]}'+'\n'
        stream2.write(data)
    stream2.close()
except IOError as e:
    print('Error:',strerror(e.errno))