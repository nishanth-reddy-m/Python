inp = input().replace(' ','').lower()
if inp == inp[::-1]:
    print('It\'s a palindrome')
else:
    print('It\'s not a palindrome')