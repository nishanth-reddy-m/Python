class HashTable:
    def __init__(self):
        self.storage = 10
        self.array = [[] for _ in range(self.storage)]
    def __hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.storage
    def __setitem__(self,key,value):
        h = self.__hash(key)
        for index,data in enumerate(self.array[h]):
            if data[0] == key:
                self.array[h][index] = (key,value)
                return
        self.array[h].append((key,value))
    def __getitem__(self,key):
        h = self.__hash(key)
        for data in self.array[h]:
            if data[0] == key:
                return data[1]
    def __delitem__(self,key):
        h = self.__hash(key)
        for index,data in enumerate(self.array[h]):
            if data[0] == key:
                del self.array[h][index]

ht = HashTable()
ht['march 1'] = 1
ht['march 6'] = 2
ht['march 17'] = 3
print(ht.array)
ht['march 6'] = 1
ht['march 17'] = 2
ht['march 1'] = 0
print(ht.array)
print(ht['march 1'],ht['march 5'],ht['march 17'])
del ht['march 1']
print(ht.array)
del ht['march 6']
print(ht.array)
del ht['march 17']
print(ht.array)