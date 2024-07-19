class prime:
    def __init__(self,num):
        self.__num = num
    def __bool__(self):
        return self.__prime()
    def __str__(self):
        if bool(prime(self.__num)):
            return f'{self.__num} is prime'
        else:
            return f'{self.__num} is not prime'
    def __prime(self,check = 2):
        if check == self.__num:
            return True
        if self.__num % check == 0:
            return False
        else:
            return self.__prime(check + 1)

class Prime(prime):
    def __init__(self,num):
        self.__num = num
        prime.__init__(self,self.__num)
        self.__list = []
        self.list = self.__getall()
    def __getall(self):
        for i in range(2,self.__num):
            if bool(prime(i)):
                self.__list.append(i)
            else:
                continue
        return self.__list
        
prime = Prime(10)
print(prime)
print(bool(prime))
print(prime.list)
