# # %%
# # string to list, list to addition, result to list if longer than 1 digit.
#
# birth_date = input('Enter your birth date as DDMMYYY: ')
#
#
# def decomposition(adsum):
#     lst = []
#     for i in str(adsum):
#         lst.append(i)
#     return lst
#
#
# def adsum(container):
#     addition = 0
#     for i in container:
#         addition += int(i)
#     return addition
#
#
# container = []
#
# for sign in birth_date:
#     if sign.isdigit():
#         container.append(sign)
#     else:
#         continue
#
# total = adsum(container)
# while len(str(total)) > 1:
#     if len(str(total)) > 1:
#         container.clear()
#         container = decomposition(total)
#         total = adsum(container)
#
# print('Your number of life is: ', total)


# # %%
# # shorter version
#
# ok = False
# while not ok:
#     birth_date = input('Enter your birth date as DDMMYYYY: ')
#     ok = birth_date.isdigit() and len(birth_date) == 8
#     if not ok:
#         birth_date = input('Date has to have exactly 8 digits: ')
#
#
# while len(birth_date) > 1:
#     total = 0
#     for digit in birth_date:
#         total += int(digit)
#     birth_date = str(total)
#
# print('Your number of life is: ', total)

