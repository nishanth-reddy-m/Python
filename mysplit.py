def mysplit(strng):
    string = ''
    mylist = []
    for i in strng:
        if i.isspace():
            if string == '':
                continue
            else:
                mylist.append(string)
                string = ''
        else:
            string += i
    if string != '':
        mylist.append(string)
    return mylist

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    