import serial.tools.list_ports

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = 'COM5'
serialInst.open()

database = {}

def arduino(inp):
    if inp == 0:
        out = 'ON'
        serialInst.write(out.encode('utf-8'))
        print('Locker locked')
    if inp == 1:
        out = 'OFF'
        serialInst.write(out.encode('utf-8'))
        print('Locker unlocked')

def register(uid,upass):
    if uid in database:
        print('User already exist')
    else:
        database[uid] = upass
        print('user =',uid,'created')

def login(uid,upass):
    if uid in database and database[uid]==upass:
        loggedin()
    else:
        print('Invalid userid or password')

def loggedin():
    log = input('Do you want to lock or unlock the locker: ').lower()
    if(log == 'lock'):
        arduino(0)
    elif(log == 'unlock'):
        arduino(1)
    else:
        print('Invalid input, Please try again')
        loggedin()

arduino(0)
while True:
    inp = input("Do you want to register or login: ").lower()
    if(inp == 'login'):
        uid = input('Enter userid: ')
        upass = input('Enter password: ')
        login(uid,upass)
    elif(inp == 'register'):
        uid = input('Enter userid: ')
        upass = input('Enter password: ')
        register(uid,upass)
    elif inp == 'exit':
        exit()
    else:
        print('Invalid input, Please try again')