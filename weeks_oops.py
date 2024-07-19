class WeekDayError(Exception):
    pass

class weeker:
    __days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    def __init__(self,string):
        try:    
            assert string in weeker.days
            self.__day = string
            self.__index = weeker.days.index(self.__day)+1
        except AssertionError:
            raise WeekDayError
    def __str__(self):
        return self.__day
    def add_days(self,num):
        self.__index = (self.__index + num) % 7
        self.__day = weeker.days[self.__index - 1]
    def subtract_days(self,num):
        return self.add_days(-num)

try:
    weekday = weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")