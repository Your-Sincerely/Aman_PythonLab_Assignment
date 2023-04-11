'''The datetime module supplies classes for manipulating dates and times.

While date and time arithmetic is supported, the focus of the implementation
is on efficient attribute extraction for output formatting and manipulation.
'''

import datetime
from datetime import date

'''class datetime.datetime
A combination of a date and a time.
Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
'''
now = datetime.datetime.now()
print(now)

'''class datetime.date
An idealized naive date, assuming the current Gregorian calendar always was,
and always will be, in effect. Attributes: year, month, and day.
'''
current_date = datetime.date.today()
print(current_date)

d = datetime.date(2023, 3, 15)
print(d)

todays_date = date.today()
print("Today's date =", todays_date)

timestamp = date.fromtimestamp(77)
print("Date =", timestamp)

today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

now = datetime.datetime.now()
t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("s2:", s2)

today = datetime.date.today()
day = int(input("Enter the number of days to add: "))
days = datetime.timedelta(days = day)
added_days = today + days
print(added_days)
