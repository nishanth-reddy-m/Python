class Queue():
    def __init__(self):
        self.__list = []
    def queueerror(self):
        print('Insert data into the queue')
        return 'None'
    def put(self,data):
        self.__list.insert(0,data)
        print(f'Updated list: {self.__list}')
    def get(self):
        try:
            var = self.__list[-1]
            del self.__list[-1]
            if self.__list == []:
                print('Queue is Empty')
            else:
                print(f'Updated list: {self.__list}')
            return var
        except IndexError:
            return self.queueerror()

def user():
    try:
        n = int(input('Enter 0 to get or 1 to put: '))
        assert n == 1 or n == 0
        if n:
            data = int(input('Enter the data: '))
            queue.put(data)
        else:
            print(f'Removed element: {queue.get()}')
    except AssertionError:
        print('Invalid Input, Try again')
        user()
    except Exception as e:
        print(f'Error: {str(e)}')
        raise KeyboardInterrupt

queue = Queue()

while True:
    try:
        user()
    except KeyboardInterrupt:
        print('\nProgram Ended')
        break