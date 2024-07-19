from os import strerror
try:
    key = int(input('Enter the key for binary.bin: ')) % 255
    readdata = open('binary.bin','rb')
    print('Decrypting the data')
    content = bytearray(readdata.read())
    print('Successfully decrypted')
    print('"',end='')
    [print(chr(i^key),end = '') for i in content]
    print('"',end='')
except IOError as e:
    print('Error:',strerror(e.errno))