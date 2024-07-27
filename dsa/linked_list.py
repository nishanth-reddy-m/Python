class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_first(self,data):
        node = Node(data,self.head)
        self.head = node
    def insert_at_last(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def extend(self, *data):
        for values in data:
            self.insert_at_last(values)
    def __iterate(self):
        if self.head is None:
            print('List is empty')
            return
        itr = self.head
        while itr:
            yield str(itr.data)
            itr = itr.next
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise IndexError('Invalid index')
        if index == 0:
            if self.head.next:
                self.head = self.head.next
                return
            self.head = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    def insert_at(self,index,data):
        if index < 0 or index > self.length():
            raise IndexError('Invalid index')
        if index == 0:
            self.insert_at_first(data)
            return
        elif index == self.length():
            self.insert_at_last(data)
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    node = itr.next
                    itr.next = Node(data,node)
                    break
                count += 1
                itr = itr.next
    def get(self,index):
        if index < 0 or index > self.length():
            raise IndexError("Invalid Index")
        count = 0
        itr = self.head
        while itr:
            if count == index:
                return itr.data
            count += 1
            itr = itr.next
    def get_all(self):
        itr = self.head
        while itr:
            yield itr.data
            itr = itr.next
    def insert_after(self,value,data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == value:
                self.insert_at(count+1,data)
                return
            count += 1
            itr = itr.next
        raise ValueError('Data not found')
    def remove(self,data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(count)
                return
            count += 1
            itr = itr.next
        raise ValueError('Data not found')
            
    def print(self):
        print(' -> '.join(list(self.__iterate())))

if __name__ == "__main__":
    ll = LinkedList()
    ll.print()
    ll.extend(2,3,4)
    ll.print()
    ll.insert_at_first(1)
    ll.print()
    ll.insert_at_last(10)
    ll.print()
    ll.insert_after(10,5)
    ll.print()
    ll.remove(10)
    print(ll.get(3))
    ll.print()
    ll.remove_at(0)
    ll.print()
    ll.insert_at(0,1)
    ll.print()
    print(ll.length())