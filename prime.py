def prime(n):
    i=2
    c=0
    while(i!=n):
        if n%i==0:
            c+=1
        i+=1
    if(c==0): return n

def allprime(n,m):
    r=[]
    while(n<=m):
        if(prime(n)!=None): r.append(n)
        n+=1
    r.sort()
    return r

def printallprimes():
    while True:
        a=input("Enter '-1' to end the program\nEnter the range of numbers[eg. 20-30]: ")
        if ('-' not in a):
            print('''\n                   Enter the valid input.
                         Example
                            |
                            V
                          20-30
                  ''')
            continue
        elif(a=='-1'): break 
        n=int(a.split('-')[0])
        m=int(a.split('-')[1])
        if(n>m):
            print('\nYou mean',str(m)+'-'+str(n),'?')
            n,m = m,n
        if(n<2): n=2
        print()
        print(allprime(n,m))
        print()

print()
printallprimes()
print("\nProgram ended\n")