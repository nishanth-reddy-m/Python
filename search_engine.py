import os
count = 0
def search(f,p = os.getcwd()):
    try:
        os.chdir(p)
    except OSError:
        return
    for dir in os.listdir('.'):
        if f in dir.lower():
            global count
            count += 1
            print(os.path.join(p,dir))
        search(f,os.path.join(p,dir))
def user():
    f = input('Enter the file/folder name: ')
    p = input('Enter the path or press enter to search in current path: ')
    if p == '':
        search(f)
    else:
        search(f,p)
if __name__ == '__main__':
    user()
    if count:
        pass
    else:
        print('File/folder not found')