from time import sleep
def timeformat(hour,minute,second):
    hour_str = str(hour)
    minute_str = str(minute)
    second_str = str(second)
    if len(hour_str) < 2:
        hour_str = '0' + hour_str
    if len(minute_str) < 2:
        minute_str = '0' + minute_str
    if len(second_str) < 2:
        second_str = '0' + second_str
    return f'{hour_str}:{minute_str}:{second_str}'

class timer:
    def __init__(self,hours = 0,minutes = 0,seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    def __str__(self):
        return timeformat(self.__hours,self.__minutes,self.__seconds)
    def next_second(self):
        self.__seconds += 1
        if self.__seconds not in range(60):
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes not in range(60):
                self.__minutes = 0
                self.__hours += 1
                if self.__hours not in range(24):
                    self.__hours = 0
    def previous_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23


n = list(map(int,input().split()))
obj = timer(n[0],n[1],n[2])
print(obj)
while True:
    obj.next_second()
    print(obj)
    sleep(1)