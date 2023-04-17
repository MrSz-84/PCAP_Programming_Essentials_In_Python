# # %%
# # String to list in reverse order, join and compare to input without spaces
# palindrom = input('Enter a text to check if it is a palindrom: ')
#
# ok = False
# while not ok:
#     if len(palindrom) != 0 and palindrom.replace(' ', '').isalpha():
#         ok = True
#     else:
#         palindrom = input('Numbers and special signs aren\'t allowed. '
#                           'Type in another text: ')
#
#
# iterated_string = []
# for letter in palindrom:
#     if letter.isspace():
#         continue
#     else:
#         iterated_string.insert(0, letter)
#
# is_palindrom = ''.join(iterated_string)
# if is_palindrom.upper() == palindrom.upper().replace(' ', ''):
#     print("It's a palindrom")
# else:
#     print("It's not a palindrom")


# # %%
# # Reverse a string and compare to input. Both without spaces
#
# palindrom = input('Enter a text to check if it is a palindrom: ')
#
# ok = False
# while not ok:
#     if len(palindrom) != 0 and palindrom.replace(' ', '').isalpha():
#         ok = True
#     else:
#         palindrom = input('Numbers and special signs aren\'t allowed. '
#                           'Type in another text: ')
#
# if palindrom[::-1].lower().replace(' ', '') == palindrom.lower().replace(' ', ''):
#     print("It's a palindrom")
# else:
#     print("It's not a palindrom")

# %%
# Check the first and the last letter if not true it's not a anagram

def is_it_palindrom(palindrome):
    for i in range(len(palindrome) // 2):
        check = palindrome[i] == palindrome[(i + 1) * -1]
        if int(check) != 1:
            return print("It's not a palindrom")
    return print("It's a palindrom")


palindrome = input('Enter a text to check if it is a palindrom: ')

ok = False
while not ok:
    if len(palindrome) != 0 and palindrome.replace(' ', '').isalpha():
        ok = True
    else:
        palindrome = input('Numbers and special signs aren\'t allowed. '
                          'Type in another text: ')

palindrome = palindrome.replace(' ', '').lower()

is_it_palindrom(palindrome)
