class Node:
    def __init__(self,previous=None,data=None,next=None):
        self.prev = previous
        self.data = data
        self.next = next
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_first(self,data):
        if self.head is None:
            node = Node(data=data,next = self.head)
            self.head = node
        else:
            node = Node(data=data,next = self.head)
            self.head.prev = node
            self.head = node
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
    def insert_at_last(self,data):
        if self.head is None:
            self.insert_at_first(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(itr,data,None)
    def extend(self,*data):
        for values in data:
            self.insert_at_last(values)
    def insert_at(self,index,data):
        if index < 0 or index > self.length():
            raise IndexError("Invalid Index")
        if index == 0:
            self.insert_at_first(data)
            return
        if index == self.length():
            self.insert_at_last(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(itr,data,itr.next)
                node.next.prev = node
                itr.next = node
                return
            count += 1
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
        raise ValueError('Value not found')
    def remove_at(self,index):
        if index < 0 or index >= self.length():
            raise IndexError("Invalid Index")
        if index == 0:
            if self.head.prev:
                self.head = self.head.next
                self.head.prev = None
                return
            self.head = None
            return
        if index == self.length() - 1:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = None
                    return    
                count += 1
                itr = itr.next
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next.next.prev = itr
                itr.next = itr.next.next
                return
            count += 1
            itr = itr.next
    def remove(self,data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(count)
                return
            count += 1
            itr = itr.next
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def forward(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            itr = self.head
            while itr:
                yield str(itr.data)
                itr = itr.next
    def reverse(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            while itr:
                yield str(itr.data)
                itr = itr.prev
    def print(self,reverse=False):
        if reverse:
            print(' <- '.join(list(self.reverse())))
        else:
            print(' -> '.join(list(self.forward())))
                
if __name__ == '__main__':
    dl = DoubleLinkedList()
    dl.extend(2,3,4)
    dl.print()
    dl.print(True)
    dl.insert_at_first(1)
    dl.print()
    dl.print(True)
    dl.insert_at_last(5)
    dl.print()
    dl.print(True)
    dl.insert_at(4,6)
    dl.print()
    dl.print(True)
    dl.remove(6)
    dl.print()
    dl.print(True)
    dl.insert_after(5,6)
    dl.print()
    print(dl.get(3))
    dl.print(True)
    dl.print()
    dl.remove_at(dl.length() - 1)
    dl.print()
    dl.print(True)
    print(dl.length())