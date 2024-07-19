def a(n):
    return f'a{n}:'
    
def q1():
    '''
    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
        got a refund of 200$. Make a correction to your monthly expense list
        based on this
    '''
    exp = [2200, 2350, 2600, 2130, 2190]
    print(exp)
    print(a(1),exp[1] - exp[0])
    print(a(2),exp[0]+exp[1]+exp[2])
    print(a(3),2000 in exp)
    exp.append(1980)
    print(a(4),exp)
    exp[3] = exp[3] + 200
    print(a(5),exp)

def q2():
    '''
    1. Length of the list
    2. Add 'black panther' at the end of this list
    3. You realize that you need to add 'black panther' after 'hulk',
        so remove it from the list first and then add it after 'hulk'
    4. Now you don't like thor and hulk because they get angry easily :)
        So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
        Do that with one line of code.
    5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
    '''
    heros = ['spider man','thor','hulk','iron man','captain america']
    print(heros)
    print(a(1),len(heros))
    heros.append('black panther')
    print(a(2),heros)
    heros.remove('black panther')
    heros.insert(heros.index('hulk')+1,'black panther')
    print(a(3),heros)
    heros[heros.index('thor'):(heros.index('hulk')+1)] = ['doctor strange']
    print(a(4),heros)
    heros.sort()
    print(a(5),heros)

def q3():
    n = int(input('Enter a number: '))
    list_ = list(filter(lambda x:x%2 != 0,range(n+1)))
    print(list_)

q1()
print()
q2()
print()
q3()