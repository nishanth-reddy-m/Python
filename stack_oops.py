class stack:
    def __init__(self):
        print('This is an implementation of stack')
        self.__list = []
    def push(self,data):
        self.__list.append(data)
        print(f'Updated list: {self.__list}')
    def pop(self):
        try:
            var = self.__list[-1]
            del self.__list[-1]
            print(f'Updated list: {self.__list}')
            return var
        except (IndexError):
            print('Stack is empty')
            return 0

class stacksum(stack):
    def __init__(self):
        stack.__init__(self)
        self.__sum = 0
    def push(self,data):
        self.__sum += data
        stack.push(self,data)
    def pop(self):
        data = stack.pop(self)
        self.__sum -= data
    def sumreturn(self):
        return self.__sum

def user():
    x = int(input('Enter 1 to push or 0 to pop: '))
    if x:
        n = int(input('Enter the data: '))
        stacks.push(n)
        print(f'Sum of list: {stacks.sumreturn()}')
    else:
        stacks.pop()
        print(f'Sum of list: {stacks.sumreturn()}')

stacks = stacksum()

try:
    while True:
        user()
except KeyboardInterrupt:
    print('\nProgram ended')