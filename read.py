from os import strerror

try:
    spl = space = chars = num = alpha = count = maxcount = 0
    stream = open('write.txt','rt')
    file = open('write.txt','rt')
    line = open('write.txt','rt')
    filecontent = file.read()
    content = stream.readline()
    lines = line.readlines()
    while content != '':
        for char in content:
            if not (char.isalnum() or char.isspace() or char == '\n'):
                spl += 1
            if char.isalpha():
                alpha += 1
            if char.isdigit():
                num += 1
            elif char.isspace() and char != '\n':
                space += 1
            else:
                chars += 1
            count += 1
        if count > maxcount:
            maxcount = count
        count = 0
        content = stream.readline()
    print('-'*maxcount)
    print(filecontent)
    print('-'*maxcount)
    print('Chars:',chars)
    print('Alphabets:',alpha)
    print('Numbers:',num)
    print('Special Chars:',spl)
    print('Spaces:',space)
    print('Lines:',len(lines))
    file.close()
    stream.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))