n = input()
if n.isalpha():
    n = list(n)
    data = ''.join(list(map(lambda x:str(ord(x))+' ',n)))
else:
    n = map(int,n.split())
    data = ''.join(list(map(str,map(lambda x:chr(x),n))))
print(data)
