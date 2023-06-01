# %% The Timer class ---> My solution
class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.__seconds_bucket = hour * 3600 + minute * 60 + second
        self.__hour = self.__seconds_bucket // 3600 % 24
        self.__min = self.__seconds_bucket // 60 % 60
        self.__sec = self.__seconds_bucket - self.__min * 60 - self.__hour * 3600

    def __str__(self):
        self.__d_hour = str(1)
        self.__d_min = 1
        self.__d_sec = 1
        return f"{self.__hour:02d}:{self.__min:02d}:{self.__sec:02d}"

    def next_second(self):
        self.__seconds_bucket += 1
        self.__hour = self.__seconds_bucket // 3600 % 24
        self.__min = self.__seconds_bucket // 60 % 60
        self.__sec = self.__seconds_bucket % 60

    def prev_second(self):
        self.__seconds_bucket -= 1
        self.__hour = (self.__seconds_bucket // 3600) % 24
        self.__min = self.__seconds_bucket // 60 % 60
        self.__sec = self.__seconds_bucket % 60


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)


# %% The Timer class ---> Sample course solution
# def two_digits(val):
#     s = str(val)
#     if len(s) == 1:
#         s = '0' + s
#     return s
#
#
# class Timer:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds
#
#     def __str__(self):
#         return two_digits(self.__hours) + ":" + \
#             two_digits(self.__minutes) + ":" + \
#             two_digits(self.__seconds)
#
#     def next_second(self):
#         self.__seconds += 1
#         if self.__seconds > 59:
#             self.__seconds = 0
#             self.__minutes += 1
#             if self.__minutes > 59:
#                 self.__minutes = 0
#                 self.__hours += 1
#                 if self.__hours > 23:
#                     self.__hours = 0
#
#     def prev_second(self):
#         self.__seconds -= 1
#         if self.__seconds < 0:
#             self.__seconds = 59
#             self.__minutes -= 1
#             if self.__minutes < 0:
#                 self.__minutes = 59
#                 self.__hours -= 1
#                 if self.__hours < 0:
#                     self.__hours = 23
#
#
# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)
