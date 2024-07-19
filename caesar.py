#Caesar cipher

def encrypt():
    data = input('Text to be encrypted: ')
    cycle = int(input('Enter the skip count: '))
    cycle %= 26
    cipher = ''
    for i in data:
        if i.isalpha():
            uni = ord(i)+cycle
            if i >= 'a' and i <= 'z':
                if uni > ord('z'):
                    uni = ord('a') + (uni-ord('z')) - 1
            if i >= 'A' and i <= 'Z':
                if uni > ord('Z'):
                    uni = ord('A') + (uni-ord('Z')) - 1
            cipher += chr(uni)
        else:
            cipher += i
    print('Encrypted text: ',cipher)

def decrypt():
    data = input('Text to be decrypted: ')
    cycle = int(input('Enter the skip count: '))
    cycle %= 26
    cipher = ''
    for i in data:
        if i.isalpha():
            uni = ord(i)-cycle
            if i >= 'a' and i <= 'z':
                if uni < ord('a'):
                    uni = ord('z') - (ord('a')-uni) + 1
            if i >= 'A' and i <= 'Z':
                if uni < ord('A'):
                    uni = ord('Z') - (ord('A')-uni) + 1
            cipher += chr(uni)
        else:
            cipher += i
    print('Decrypted text: ',cipher)
    
inp = int(input('Enter \'1\' for Encryption \'0\' for Decryption: '))
if inp == 1:
    encrypt()
elif inp == 0:
    decrypt()
else:
    print('Invalid Input')