'''
2020/11/04 14:53:00
20/November/04 02:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309
Week number of the year: 44
'''

from datetime import datetime
dt = datetime(2020,11,4,14,53,0)
print(dt.strftime('%Y/%m/%d %X'))
print(dt.strftime('%y/%B/%d %I:%M:%S %p'))
print(dt.strftime('%a, %Y %b %d'))
print(dt.strftime('%A, %Y %B %d'))
print('Weekday:',dt.strftime('%w'))
print('Day of the year:',dt.strftime('%j'))
print('Week number of the year:',dt.strftime('%W'))