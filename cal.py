import calendar
import datetime
calendar.setfirstweekday(calendar.SUNDAY)
#print(calendar.calendar(2024,w=4,l=2,c=10,m=4))
#calendar.prcal(2024,w=4,l=2,c=10,m=4)
calendar.prmonth(2002,calendar.JANUARY,w=4,l=2)
print(calendar.weekday(2002,calendar.JANUARY,22))