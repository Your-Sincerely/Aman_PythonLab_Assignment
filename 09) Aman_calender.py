# Python program to display calendar of 2023
# given month of the year

'''The calendar module allows output calendars like the program and provides
additional useful functions related to the calendar. Functions and classes defined
in the calendar module use an idealized calendar, the current Gregorian calendar extended
indefinitely in both directions. By default, these calendars have Monday as the first day
of the week, and Sunday as the last (the European convention).
'''

# import module
import calendar

month = 1
while month < 13:
    print(calendar.month(2023, month))  # prints calendar of the month
    month += 1


def year():
    print(calendar.calendar(2023))  # prints all months of the year (in tabular form)


def month():
    print(calendar.month(2023, 2))  # prints the given month which is provided


def gap():
    print(calendar.month(2023, 2, 5))  # here 5 provides the space between dates


