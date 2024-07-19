def generator(n):
    for i in range(n):
        yield i

n = int(input())
gdata = generator(n)
print('Generator before use',list(gdata))
print('Generator after use',list(gdata))