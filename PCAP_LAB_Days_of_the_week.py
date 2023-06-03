# %% PCAP LAB ---> My solution lists
class WeekDayError(Exception):
    pass


class Weeker:
    __days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        self.__day = day
        if self.__day not in self.__days:
            raise WeekDayError
        self.__day_number = self.__days.index(self.__day)

    def __str__(self):
        return self.__days[self.__day_number]

    def add_days(self, n):
        self.__day_number = (self.__day_number + n) % 7

    def subtract_days(self, n):
        self.__day_number = (self.__day_number - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(4)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")


# %% PCAP LAB ---> My solution dicts

class WeekDayError(Exception):
    pass


class Weeker:
    __days = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}

    def __init__(self, day):
        self.__day = day
        if self.__day not in self.__days.keys():
            raise WeekDayError
        self.__day_number = self.__days[self.__day]

    def __str__(self):
        return f"{dict((v, k) for k, v in self.__days.items()).get(self.__day_number)}"

    def add_days(self, n):
        self.__day_number += n
        while self.__day_number > 7:
            self.__day_number = 0 + (self.__day_number - 7)

    def subtract_days(self, n):
        self.__day_number -= n
        while self.__day_number < 1:
            self.__day_number = 7 + (self.__day_number)


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(4)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

# %% Sample solution


class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
