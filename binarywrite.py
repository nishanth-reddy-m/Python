from os import strerror
n = input('Enter the data: ')
k = int(input('Enter a key: ')) % 255
writedata = bytearray(len(n))
for i in range(len(writedata)):
    writedata[i] = ord(n[i]) ^ k
try:
    writefile = open('binary.bin','wb')
    print(f'Encrypting your data into binary.bin')
    writefile.write(writedata)
    writefile.close()
    print('Bin file created')
except IOError as e:
    print('Error:',strerror(e.errno))