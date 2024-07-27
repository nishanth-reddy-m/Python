from dl_list import DoubleLinkedList
class Queue:
    def __init__(self):
        self.__items = DoubleLinkedList()
    def enqueue(self,data):
        return self.__items.insert_at_first(data)
    def dequeue(self):
        return self.__items.remove_at(self.__items.length() - 1)
    def peek(self):
        return self.__items.get(self.__items.length() - 1)
    def size(self):
        return self.__items.length()
    def print(self):
        print(list(self.__items.get_all()))
    def return_queue(self):
        return list(self.__items.get_all())

def Lab(n):
    q = Queue()
    q.enqueue('1')
    for _ in range(n):
        print(q.peek())
        q.enqueue(q.peek()+'0')
        q.enqueue(q.peek()+'1')
        q.dequeue()

if __name__ == '__main__':
    queue = Queue()
    for i in range(11):
        queue.enqueue(i)
    queue.print()
    queue.dequeue()
    queue.print()
    Lab(10)