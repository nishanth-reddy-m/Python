inp1 = input('Enter the first word: ').replace(' ','').lower()
inp2 = input('Enter the second word: ').replace(' ','').lower()
if all(i in inp2 for i in inp1) and all(i in inp1 for i in inp2):
    print('Anagrams')
else:
    print('Not Anagrams')
