numbers = [
    ['111','101','101','101','111'],
    ['001','001','001','001','001'],
    ['111','001','111','100','111'],
    ['111','001','111','001','111'],
    ['101','101','111','001','001'],
    ['111','100','111','001','111'],
    ['111','100','111','101','111'],
    ['111','001','001','001','001'],
    ['111','101','111','101','111'],
    ['111','101','111','001','111']
    ]

def analognum(num,s1='#',s2='#'):
    r1,r2,r3,r4,r5 = [],[],[],[],[]
    for i in num:
        r1.append(' '.join(list(numbers[int(i)][0].replace('1',s1).replace('0',' '))))
        r2.append(' '.join(list(numbers[int(i)][1].replace('1',s2).replace('0',' '))))
        r3.append(' '.join(list(numbers[int(i)][2].replace('1',s1).replace('0',' '))))
        r4.append(' '.join(list(numbers[int(i)][3].replace('1',s2).replace('0',' '))))
        r5.append(' '.join(list(numbers[int(i)][4].replace('1',s1).replace('0',' '))))
    return r1,r2,r3,r4,r5

def display(userinput):
    r1,r2,r3,r4,r5 = analognum(userinput)
    print('   '.join(r1))
    print('   '.join(r2))
    print('   '.join(r3))
    print('   '.join(r4))
    print('   '.join(r5))

userinput = input('Enter a number: ')
display(userinput)