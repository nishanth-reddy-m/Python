from dl_list import DoubleLinkedList
class Stack:
    def __init__(self):
        self.__items = DoubleLinkedList()
    def push(self,data):
        return self.__items.insert_at_last(data)
    def pop(self): 
        popped = self.peek()
        self.__items.remove_at(self.__items.length()-1)
        return popped
    def peek(self):
        return self.__items.get(self.__items.length() - 1)
    def size(self):
        return self.__items.length()
    def print(self,stack_view=True):
        if stack_view:
            i = self.__items.length() - 1
            while i >= 0:
                print(self.__items.get(i))
                i -= 1
            print()
        else:
            print(list(self.__items.get_all()))
    def return_stack(self):
        return list(self.__items.get_all())

def lab1(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    size = stack.size()
    while size:    
        print(stack.pop(),end='')
        size = stack.size()
    print()
def lab2(string):
    stack = Stack()
    check = {'[':']','(':')','{':'}'}
    for char in string:
        if char in check.keys():
            stack.push(char)
        if char in check.values():
            if not stack.size():
                print('No opening brackets found')
                print()
                return
            if check[stack.peek()] == char:
                stack.pop()
    if not stack.size():
        print('String is balanced')
        print()
    else:
        print('String is unbalance')
        print('The following brackets are not closed',str(stack.return_stack()).strip('[]'))
        print()

if __name__ == '__main__':
    stack = Stack()
    for i in range(10,-1,-1):
        stack.push(i)
    stack.print(False)
    print(stack.pop())
    stack.print(False)
    print()
    lab1('We will conquere COVID-19')
    lab1('Malayalam')
    print()
    lab2("({a+b})")
    lab2("))((a+b}{")
    lab2("((a+b)))")
    lab2("(((a+g))")
    lab2("[a+b]*(x+2y)*{gg+kk}")
    lab2("[[[[{{{{((())}}]]]")