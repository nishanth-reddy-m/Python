def position(p):
    p=str(p)
    t=''
    for i in p:
        if(i=='1'): t+='^'
        else: t+=' '
    print(t)

def check():    #under progress
    print('''   
        Enter \'a\' to sort the list in ascending order 
        Enter \'d\' to sort the list in descending order    
        Enter the input: ''',end='')
    o=input()
    next()
    if(o=='a' or o=='d' or o=='A' or o=='D'):
        if(o=='a' or o=='A'): 
            print('You choose Ascending order')
            next()
            return '>'
        if(o=='d' or o=='D'): 
            print('You choose Descending order')
            next()
            return '<'
    else:
        print('\nInvalid Input, Try again')
        next()
        return check()

def instrustions():
    next()
    print('''   Welcome to Interactive sorting illustration
                List is represented as                        [0,1,2,3,4,5]
                The '^' represents the current position              ^ ^   
                                    Lets gooo                                   ''')
    next()

def next():
    dummy=input('\nPress enter to continue or \'exit\' to end the program:\n')
    if(dummy=='exit'): exit()
    print('\n\n\n\n\n\n\n\n\n')

def bubblesort(l,a,p):
    print('\nYour list ->',a)
    next()
    c=1
    s=p[:]
    while(l>0):
        if(l>1):
            print('\nIteration',c,'\n')
            next()
        for i in range(l-1):
            if(a[i]>a[i+1]):                # a[i]>a[i+1]->ascending order # a[i]<a[i+1]->descending order
                p[i]=p[i+1]=1
                print(a)
                position(p)
                print()
                print(a[i],'is greater than',str(a[i+1])+', So swap')
                next()
                a[i],a[i+1]=a[i+1],a[i]
                print(a)
                position(p)
                print('\nAfter swapping',a[i],'&',str(a[i+1])+'. This is the updated list')
                next()
                p[i]=p[i+1]=0
            else:
                p[i]=p[i+1]=1
                print(a)
                position(p)
                print()
                print(a[i],'is lesser than or equal to '+str(a[i+1])+', So skip swapping')
                next()
                p[i]=p[i+1]=0
                continue
        l-=1
        if(l>1):
            print('End of Iteration',c,'->',a,'\n')
            next()
        s[c*(-1)]=1
        print(a)
        position(s)
        print()
        print('The following value(s) are sorted, So this value(s) will not be checked in the next iterations')
        next()
        c+=1
    print('\nThe final Sorted list using bubble sort ->',a,'\n\n\n')

def user_input():
    l=int(input('\nEnter length of list: '))
    print()
    a=[]
    p=[0 for i in range(l)]
    for i in range(l):
        print('Enter value '+str(i+1)+' :',end='')
        a.append(int(input()))
    return l,a,p

instrustions()
l,a,p=user_input()
bubblesort(l,a,p)