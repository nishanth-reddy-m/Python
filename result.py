class studentdata(Exception):
    pass

class badline(studentdata):
    def __init__(self,line,content):
        super().__init__()
        self.line = line
        self.content = content

class fileempty(studentdata):
    def __init__(self):
        super().__init__()

from os import strerror

n = input('Enter the file name: ')
dictionary = {}
try:
    file = open(n+'.txt','rt')
    content = file.readlines()
    if len(content) == 0:
        raise fileempty
    for line in content:
        data = line.split()
        if len(data) != 3:
            raise badline(content.index(line),line)
        try:
            dictionary[f'{data[0]}\t{data[1]}'] += float(data[2])
        except KeyError:
            dictionary[f'{data[0]}\t{data[1]}'] = float(data[2])
    for key in sorted(dictionary.keys()):
        print(f'{key}\t{dictionary[key]}')
except IOError as e:
    print('Error:',strerror(e.errno))
except fileempty:
    print('File is empty')
except badline as e:
    print(f'Error at Line {e.line} : {e.content}')