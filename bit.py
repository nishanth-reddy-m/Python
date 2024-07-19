def adjust(x, y, z):
    x = bin(x)[2:]
    y = bin(y)[2:]
    z = bin(z)[2:]
    l = max(len(x),len(y),len(z))
    while (len(x)!=l or len(y)!=l or len(z)!=l):
        if len(x)!=l: x='0'+x
        if len(y)!=l: y='0'+y
        if len(z)!=l: z='0'+z
    return x,y,z,l
    
def bitgui():
    while(True):
        print()
        n=input("Enter '-1' to exit\nEnter the expression eg[2&3,2|3]: ")
        if('&' in n):
            a=int(n.split('&')[0])
            b=int(n.split('&')[1])
            r=a&b
        elif('|' in n):
            a=int(n.split('|')[0])
            b=int(n.split('|')[1])
            r=a|b
        elif('^' in n):
            a=int(n.split('^')[0])
            b=int(n.split('^')[1])
            r=a^b
        elif('-1' in n): break
        else: 
            print('\nInvalid operand!\n')
            continue
        bit=adjust(a,b,r)
        print()
        print(' ',bit[0],'->',a)
        print(' ',bit[1],'->',b)
        print(' ','-'*bit[3])
        print(' ',bit[2],'->',r)
        print(' ','-'*bit[3])
        print()

bitgui()
print('\nProgram Ended\n')