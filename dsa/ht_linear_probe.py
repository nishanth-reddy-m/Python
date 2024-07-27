class HashTableFull(Exception):
    def __init__(self):
        super().__init__('The HashTable is Full')
class HashTable:
    def __init__(self):
        self.storage = 10
        self.array = [None for _ in range(self.storage)]
    def __hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.storage
    def __setitem__(self,key,value):
        h = self.__hash(key)
        if self.array[h] is None:
            self.array[h] = (key,value)
        else:
            new_h = self.__linear_probe(key,h)
            self.array[new_h] = (key,value)
    def __getitem__(self,key):
        h = self.__hash(key)
        probe_range = self.__get_range(h)
        for probe_index in probe_range:
            if self.array[probe_index] is None:
                continue
            if self.array[probe_index][0] == key:
                return self.array[probe_index][1]
        raise KeyError('Key not found')
    def __delitem__(self,key):
        h =self.__hash(key)
        probe_range = self.__get_range(h)
        for probe_index in probe_range:
            if self.array[probe_index] is None:
                continue
            if self.array[probe_index][0] == key:
                self.array[probe_index][1] = None
                return
        raise KeyError('Key not found')
    def __get_range(self,index):
        return [*range(index,self.storage)] + [*range(0,index)]
    def __linear_probe(self,key,index):
        probe_range = self.__get_range(index)
        for probe_index in probe_range:
            if self.array[probe_index] is None:
                return probe_index
            if self.array[probe_index][0] == key:
                return probe_index
        raise HashTableFull
ht = HashTable()
for i in range(10):
    ht[f'march {i}'] = i
print(ht.array)
ht['march 0'] = 10
print(ht.array)