class myexceptions(Exception):
    def __init__(self,message):
        Exception.__init__(self,message)

class alphaerror(myexceptions):
    def __init__(self):
        super().__init__('Alphabets invalid')

class specialerror(myexceptions):
    def __init__(self):
        super().__init__('Special Characters invalid')

def test():
    inp = input('Only digits are valid!: ')
    if inp.isdigit():
        print('OK')
    elif inp.isalnum():
        raise alphaerror
    else:
        raise specialerror

while True:
    try:
        test()
    except KeyboardInterrupt:
        break
    except myexceptions:
        print('myexceptions raised')
        raise