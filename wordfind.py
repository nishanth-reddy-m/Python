inp1 = input().lower()
inp2 = input().lower()
found = all(i in inp2 for i in inp1)
if found:
    print('Yes')
else:
    print('No')