class Fib:
    def __init__(self,num):
        self.__num = num
        self.__f = self.__s = self.__c = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.__c > self.__num:
            raise StopIteration
        if self.__c == 1:
            self.__c += 1
            return self.__f
        else:
            c = self.__f + self.__s
            self.__f,self.__s = self.__s,c
            self.__c += 1
            return self.__f

class fib:
    def __init__(self,num):
        self.__num = num
        self.__f = self.__s = self.__c = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.__c == 1:
            self.__c += 1
            return self.__f
        else:
            c = self.__f + self.__s
            self.__f,self.__s = self.__s,c
            self.__c += 1
            if self.__f > self.__num:
                raise StopIteration
            return self.__f

obj1 = Fib(10)
obj2 = fib(10)

for i in obj1:
    print(i)
print()

for i in obj2:
    print(i)