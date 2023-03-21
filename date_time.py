import datetime
from datetime import date

# write a python program to add some dates to the present date and print the day

# to print the date(yyyy-mm-dd) and time
now = datetime.datetime.now()
print(now)

# To print the current date(yyyy-mm-dd)
current_date = datetime.date.today()
print(current_date)

# To print a specific date(yyyy-mm-dd)
d = datetime.date(2023, 3, 15)
print(d)

# today() to get current date
todays_date = date.today()
print("Today's date =", todays_date)

# timestamp = january1, 1970
timestamp = date.fromtimestamp(77)  # adds 77 seconds to the timestamp
print("Date =", timestamp)

# to print today's year, month, day
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# formats of date and time
now = datetime.datetime.now()
t = now.strftime("%H:%M:%S")
print("Time:", t)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

# To add days to present date and tell the date:
today = datetime.date.today()
day = int(input("Enter the number of days to add: "))
days = datetime.timedelta(days = day)
added_days = today + days
print(added_days)
