# Leap Normal Tear function

# def if_leap(year):
#     if year < 1582:
#         return False
#     else:
#         if year % 4 != 0:
#             return False
#         elif year % 100 != 0:
#             return True
#         elif year % 400 != 0:
#             return False
#         else:
#             return True

# # test_data = []
# # check = True
# # while check:
# #     year = int(input("Enter a year or '-1' to exit:"))
# #     if year == -1:
# #         break
# #     test_data.append(year)
    

# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     r = test_data[i]
#     print(r, "->", end="")
#     result = if_leap(r)
#     if result == test_results[i]:
#         print("Positive results")
#     else:
#         print("Negative results")

# Leap normal year and month's length function

# def if_leap(year):
#     if year < 1582:
#         return False
#     else:
#         if year % 4 != 0: # normal year
#             return False
#         elif year % 100 != 0: # leap year
#             return True
#         elif year % 400 != 0: # normal year
#             return False
#         else:
#             return True # leap year

# def month_length(year, month):
#     a = if_leap(year)
#     if a:
#         if month == 2:
#             return(29)
#         elif month not in [4, 6, 9, 11]:
#             return(31)
#         else:
#             return(30)
#     else:
#         if month == 2:
#             return(28)
#         elif month not in [4, 6, 9, 11]:
#             return(31)
#         else:
#             return(30)

# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 5, 1, 11]
# test_days = [28, 31, 31, 30]
# for i in range(len(test_years)):
# 	r = test_years[i]
# 	m = test_months[i]
# 	print(r, m, "-> ", end="")
# 	result = month_length(r, m)
# 	if result == test_days[i]:
# 		print("OK")
# 	else:
# 		print("Test negative")


# def czy_przestepny(rok):
# 	if rok % 4 != 0:
# 		return False
# 	elif rok % 100 != 0:
# 		return True
# 	elif rok % 400 != 0:
# 		return False
# 	else:
# 		return True

# def dni_w_miesiacu(rok, miesiac):
# 	if rok < 1582 or miesiac < 1 or miesiac > 12:
# 		return None
# 	dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 	wyn = dni[miesiac - 1]
# 	if miesiac == 2 and czy_przestepny(rok):
# 		wyn = 29
# 	return wyn

# testuj_lata = [1900, 2000, 2016, 1987]
# testuj_miesiace = [ 2, 2, 1, 11]
# testuj_wynik = [28, 29, 31, 30]
# for i in range(len(testuj_lata)):
# 	r = testuj_lata[i]
# 	m = testuj_miesiace[i]
# 	print(r, m, "-> ", end="")
# 	wynik = dni_w_miesiacu(r, m)
# 	if wynik == testuj_wynik[i]:
# 		print("OK")
# 	else:
# 		print("Nie powiodło się")


# Leap Normal year month's length and day of the year function

# def if_leap(year):
#     if year < 1582:
#         return None
#     else:
#         if year % 4 != 0: # normal year
#             return False
#         elif year % 100 != 0: # leap year
#             return True
#         elif year % 400 != 0: # normal year
#             return False
#         else:
#             return True # leap year

# def month_length(year, month):
#     a = if_leap(year)
#     if a:
#         if month == 2:
#             return(29)
#         elif month is not [4, 6, 9, 11]:
#             if month == True:
#                 return(31)
#             else:
#                 return(30)
#     else:
#         if month == 2:
#             return(28)
#         elif month is not [4, 6, 9, 11]:
#             if month == True:
#                 return(31)
#             else:
#                 return(30)
            
# def day_of_the_year(year, month, day):
#     leap = if_leap(year)

#     if month > 12 or month < 1 or year < 1582 or day < 1 or day > 31 or if_leap == None:
#         None


#     elif leap == True:
#         days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         days_counter = 0
#         for i in range(month-1):
#             days_counter += days[i]
#         return(days_counter + day)
    
#     elif leap == False:
#         days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         days_counter = 0
#         for i in range(month-1):
#             days_counter += days[i]
#         return(days_counter + day)

# print(day_of_the_year(2000, 12, 31))
# print(day_of_the_year(1992, 8, 17))
# print(day_of_the_year(2007, 6, 15))
# print(day_of_the_year(2015, 2, 3))
# print(day_of_the_year(2128, 8, 15))
# print(day_of_the_year(1992, 7, 22))


# Leap Normal year month's length and day of the year function

# def if_leap(year):
#     if year < 1582:
#         return None
#     else:
#         if year % 4 != 0: # normal year
#             return False
#         elif year % 100 != 0: # leap year
#             return True
#         elif year % 400 != 0: # normal year
#             return False
#         else:
#             return True # leap year
#
# def month_length(year, month):
#     a = if_leap(year)
#     if a:
#         if month == 2:
#             return(29)
#         elif month not in [4, 6, 9, 11]:
#             return(31)
#         else:
#             return(30)
#     else:
#         if month == 2:
#             return(28)
#         elif month not in [4, 6, 9, 11]:
#             return(31)
#         else:
#             return(30)
#
# def day_of_the_year(year, month, day):
#     if month > 12 or month < 1 or year < 1582 or day < 1 or day > 31 or if_leap == None:
#         None
#
#     days_counter = 0
#
#     for i in range(1, month):
#         days_counter += month_length(year, i)
#     return(days_counter + day)
#
#
# print(day_of_the_year(2000, 12, 31))
# print(day_of_the_year(1992, 8, 17))
# print(day_of_the_year(2007, 6, 15))
# print(day_of_the_year(2015, 2, 3))
# print(day_of_the_year(2128, 8, 15))
# print(day_of_the_year(1992, 7, 22))


def is_year_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def days_in_month(year, month):
    lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1582 or month > 12 or month < 1:
        return None
    if is_year_leap(year):
        if month == 2:
            return 29
        return lst[month - 1]
    elif not is_year_leap(year):
        return lst[month - 1]


def day_of_year(year, month, day):
    day_sum = 0
    if year < 1582 or month > 12 or month < 1 or day < 1 or day > 31:
        return None
    for mt in range(month - 1):
        day_sum += days_in_month(year, mt + 1)
    return day_sum + day


print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 12, 31))
print(day_of_year(2002, 12, 30))
print(day_of_year(2004, 12, 30))
print(day_of_year(2023, 5, 3))
print(day_of_year(2000, 12, 31))
print(day_of_year(1992, 8, 17))
print(day_of_year(2007, 6, 15))
print(day_of_year(2015, 2, 3))
print(day_of_year(2128, 8, 15))
print(day_of_year(1992, 7, 22))
