import os
import sys
sys.path.append('h:\\Programming\\Python')
from search_engine import search
def create():
    os.mkdir('tree')
    os.chdir('tree')
    p = ['c','cpp','python']
    for i in range(len(p)):
        os.makedirs(p[i%3]+'/'+'others'+'/'+p[(i+1)%3])
        os.mkdir(p[i%3]+'/'+'others'+'/'+p[(i+2)%3])
    print('Tree folders created')
def delete():
    def loop():
        if parent in os.getcwd():
            if len(os.listdir('.')):    
                for dir in os.listdir('.'):
                    if len(os.listdir(dir)):
                        os.chdir(dir)
                        return loop()
                    else:
                        os.rmdir(dir)
                return loop()
            else:
                os.chdir('..')
                return loop()
        else:
            return
    try:
        os.rmdir('tree')
        print('Tree folders deleted')
    except FileNotFoundError:
        exit()
    except OSError:
        os.chdir('tree')
        parent = os.getcwd()
        loop()
        delete()
parent = os.getcwd()
os.chdir(parent)
create()
os.chdir(parent)
search('python')
os.chdir(parent)
delete()