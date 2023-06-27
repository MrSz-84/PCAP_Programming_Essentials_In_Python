# 4.5.2 Getting the current local date and creating date objects
# import datetime
#
# today = datetime.date.today()
#
# print("Today:", today)
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)

# %% date values rules
# import datetime
#
# my_date = datetime.date(2019, 11, 4)
# print(my_date)

"""
Parameter 	Restrictions
year 	The year parameter must be greater than or equal to 1 (MINYEAR constant) and less
        than or equal to 9999 (MAXYEAR constant).
month 	The month parameter must be greater than or equal to 1 and less than
        or equal to 12.
day 	The day parameter must be greater than or equal to 1 and less than or equal to
        the last day of the given month and year.
"""

# %% 4.5.3 Creating a date object from a timestamp
# import datetime
# import time

"""
The timestamp is actually the difference 
between a particular date (including time)
and January 1, 1970, 00:00:00 (UTC), 
expressed in seconds.
"""
#
# timestamp = time.time()
# print("Timestamp:", timestamp)
#
# d = datetime.date.fromtimestamp(timestamp)
# print("Date:", d)

# %% 4.5.4 Creating a date object using the ISO format
# import datetime
#
# my_date = datetime.date.fromisoformat("2019-11-04")
# print(my_date)

# %% 4.5.5 The replace() method
# import datetime
#
#
# d = datetime.date(1991, 2, 5)
# print(d)
#
# d = d.replace(year=1992, month=1, day=16)
# print(d)

# %% 4.5.6 What day of the week is it?
# import datetime
#
# d = datetime.date(2019, 11, 4)
# print(d.weekday())
#
# d2 = datetime.date(2023, 6, 25)
# print(d2.weekday())
#
# d3 = datetime.date(2019, 11, 4)
# print(d3.isoweekday())
#
# d4 = datetime.date(2023, 6, 25)
# print(d4.isoweekday())

# %% 4.5.7 Creating time objects
"""
time(hour, minute, second, microsecond, tzinfo, fold)

Parameter 	Restrictions
hour 	        The hour parameter must be greater than or equal to 0 and less than 23.
minute 	        The minute parameter must be greater than or equal to 0 and less than 59.
second 	        The second parameter must be greater than or equal to 0 and less than 59.
microsecond 	The microsecond parameter must be greater than or equal to 0 
                and less than 1000000.
tzinfo 	        The tzinfo parameter must be a tzinfo subclass object or None (default).
fold 	        The fold parameter must be 0 or 1 (default 0).

The tzinfo parameter is associated with time zones, 
while fold is associated with wall times. 
We won't use them during this course, 
but we encourage you to familiarize yourself with them.
"""

# import datetime
#
# t = datetime.time(14, 53, 20, 1)
#
# print("Time:", t)
# print("Hour:", t.hour)
# print("Minute:", t.minute)
# print("Second:", t.second)
# print("Microsecond:", t.microsecond)
# print("Timezone:", t.tzinfo)
# print("Fold:", t.fold)

# %% The time mopdule
# import time
#
# class Student:
#     def take_nap(self, second):
#         print("I'm very tired. I have to take a nap. Se you later.")
#         time.sleep(second)
#         print("I slept well! I feel great!")
#
#
# student = Student()
# student.take_nap(10)


# %% 4.5.9 The ctime() function
# import time
#
# # timestamp = time.time()
# # print("Timestamp:", timestamp)
#
# timestamp = 1572879180
# print((time.ctime(timestamp)))  # returns date from timestamp
# print(time.ctime())     # returns current date from timestamp

# %% 4.5.10 The gmtime() and localtime() functions

"""
Some of the functions available in the time module require knowledge 
of the struct_time class, but before we get to know them, 
let's see what the class looks like:

time.struct_time:
    tm_year   # Specifies the year.
    tm_mon    # Specifies the month (value from 1 to 12)
    tm_mday   # Specifies the day of the month (value from 1 to 31)
    tm_hour   # Specifies the hour (value from 0 to 23)
    tm_min    # Specifies the minute (value from 0 to 59)
    tm_sec    # Specifies the second (value from 0 to 61 )
    tm_wday    # Specifies the weekday (value from 0 to 6)
    tm_yday   # Specifies the year day (value from 1 to 366)
    tm_isdst  # Specifies whether daylight saving time applies (1 – yes, 0 – no, 
                -1 – it isn't known)
    tm_zone   # Specifies the timezone name (value in an abbreviated form)
    tm_gmtoff # Specifies the offset east of UTC (value in seconds)

The struct_time class also allows access to values using indexes. Index 0 returns 
the value in tm_year, while 8 returns the value in tm_isdst.

The exceptions are tm_zone and tm_gmoff, which cannot be accessed using indexes.

The example shows two functions that convert the elapsed time from the Unix epoch 
to the struct_time object. The difference between them is that the gmtime function 
returns the struct_time object in UTC, while the localtime function returns local time. 
For the gmtime function, the tm_isdst attribute is always 0.

"""

# import time
#
# timestamp = 1572879180
# print(time.gmtime(timestamp))
# print(time.localtime(timestamp))


# %% 4.5.11 The asctime() and mktime() functions
# import time
#
# timestamp = 1572879180
# st = time.gmtime(timestamp)
#
#
# print(time.asctime(st))
# print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

"""


The first of the functions, called asctime, converts a struct_time object or a tuple 
to a string. Note that the familiar gmtime function is used to get the struct_time object.
If you don't provide an argument to the asctime function, the time returned 
by the localtime function will be used.

The second function called mktime converts a struct_time object or a tuple that expresses
the local time to the number of seconds since the Unix epoch. In our example, we passed a 
tuple to it, which consists of the following values:

2019 => tm_year
11 => tm_mon
4 => tm_mday
14 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst

"""

# %% 4.5.12 Creating datetime objects

"""
In the datetime module, date and time can be represented either as separate objects or as 
one object. The class that combines date and time is called datetime.

datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

Its constructor accepts the following parameters:
Parameter 	Restrictions
year 	        The year parameter must be greater than or equal to 1 (MINYEAR constant) 
                and less than or equal to 9999 (MAXYEAR constant).
month 	        The month parameter must be greater than or equal to 1 and less than 
                or equal to 12.
day 	        The day parameter must be greater than or equal to 1 and less than 
                or equal to the last day of the given month and year.
hour 	        The hour parameter must be greater than or equal to 0 and less than 23.
minute 	        The minute parameter must be greater than or equal to 0 and less than 59.
second 	        The second parameter must be greater than or equal to 0 and less than 59.
microsecond 	The microsecond parameter must be greater than or equal to 
                0 and less than 1000000.
tzinfo 	        The tzinfo parameter must be a tzinfo subclass object or None (default).
fold 	        The fold parameter must be 0 or 1 (default 0).
"""

# import datetime
#
# my_date = datetime.datetime(2019, 11, 4, 14, 53, 0)
# print("Datetime:", my_date)
# print("Date:", my_date.date())
# print("Time:", my_date.time())


# %% 4.5.13 Methods that return current date and time
# import datetime
#
# print("today:", datetime.datetime.today())
# print("now:", datetime.datetime.now())
# print("utcnow", datetime.datetime.utcnow())


# %% 4.5.14 Getting a timestamp
# import datetime
#
# dt = datetime.datetime(2020, 10, 4, 14, 55)
# print("Timestamp:", dt.timestamp())


# %% 4.5.15 Date and time formatting strftime()

# import datetime
#
# d = datetime.date(2020, 1, 4)
# print(d.strftime("%Y/%m/%d"))

"""

%Y – returns the year with the century as a decimal number. In our example, this is 2020.
%m – returns the month as a zero-padded decimal number. In our example, it's 01.
%d – returns the day as a zero-padded decimal number. In our example, it's 04.

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

"""

# %% Time formatting
# import datetime
#
# t = datetime.time(14, 53)
# print(t.strftime("%H:%M:%S"))
#
# dt = datetime.datetime(2020, 11, 4, 14, 53)
# print(dt.strftime("%y/%B/%d %H:%M:%S"))


# %% 4.5.16 The strftime() function in the time module

# import time
#
# timestamp = 1572879180
# st = time.gmtime(timestamp)
#
# print(time.strftime("%Y/%m/%d %H:%M:%S", st))
# print(time.strftime("%Y/%m/%d %H:%M:%S"))


"""
https://docs.python.org/3/library/time.html#time.strftime
"""

# %%4.5.17 The strptime() method
# import datetime, time
#
# print(datetime.datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
#
# print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

# %% 4.5.18 Date and time operations

# import datetime
#
# d1 = datetime.date(2020, 11, 4)
# d2 = datetime.date(2019, 11, 4)
#
# print(d1 - d2)
#
# dt1 = datetime.datetime(2020, 11, 4, 0, 0, 0)
# dt2 = datetime.datetime(2019, 11, 4, 0, 0, 0)
#
# print(dt1 - dt2)

# %% 4.5.19 Creating timedelta objects
# import datetime
# delta = datetime.timedelta(weeks=2, days=2, hours=3)
# print(delta)

"""
Of course, you can also create an object yourself. For this purpose, let's get acquainted 
with the arguments accepted by the class constructor, which are: 
days, seconds, microseconds, milliseconds, minutes, hours, and weeks. 
Each of them is optional and defaults to 0.
"""

# delta2 = datetime.timedelta(weeks=2, days=2, hours=3)
# print("Days:", delta2.days)
# print("Seconds:", delta2.seconds)
# print("Microseconds:", delta2.microseconds)

# %% timedelta operations
# import datetime
#
# delta = datetime.timedelta(weeks=2, days=2, hours=2)
# print(delta)
#
# delta2 = delta * 2
# print(delta2)
#
# d = datetime.date(2019, 10, 4) + delta2
# print(d)
#
# dt = datetime.datetime(2019, 10, 4, 14, 53) + delta2
# print(dt)


# %% 4.5.20 LAB The datetime and time modules
import datetime


obj = datetime.datetime(2020, 11, 4, 14, 53, 0)

print(obj.strftime("%Y/%m/%d %H:%M:%S"))
print(obj.strftime("%y/%B/%d %H:%M:%S %p"))
print(obj.strftime("%a, %Y/%b/%d"))
print(obj.strftime("%A, %Y/%B/%d"))
print(obj.strftime("Weekday: %w"))
print(obj.strftime("Day of the year: %j"))
print(obj.strftime("Week number of the year: %W"))
