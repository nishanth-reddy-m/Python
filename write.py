from os import strerror
def userinput():
    try:
        n = int(input('Enter a number: '))
        return n
    except:
        print('Invalid input, Try again')
        return userinput()

n = userinput()
try:
    stream = open('write.txt','wt')
    for i in range(1,11):
        string = f'{n} x {i} = {n*i}\n'
        stream.write(string)
    stream.close()
    print('write.txt created successfully')
except IOError as err:
    print('Error:',strerror(err.errno))