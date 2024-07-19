import serial
arduino = serial.Serial()
arduino.baudrate = 9600
arduino.port = 'COM5'
arduino.open()
lock = '20'
unlock = '21'
end = '2'

while True:
    send = input("Enter signal (0 for lock, 1 for unlock, 2 to end): ")
    
    if send == lock or send == unlock:
        send = send.encode('utf-8')
        arduino.write(send)
        print('Signal sent:', send)
        receive = arduino.readline().decode().strip()
        print('Response received:', receive)
    elif send == end:
        exit()
    else:
        print('Invalid input')
