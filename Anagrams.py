# %%
# Are they anagrams?

def is_valid(user_input):
    global counter
    ok = False
    while not ok:
        if len(user_input) != 0 and user_input.replace(' ', '').isalpha():
            ok = True
            counter += 1
        else:
            user_input = input('Numbers and special signs aren\'t allowed. '
                               'Type in another text: ')
    return user_input.replace(' ', '').lower()


def string_to_list(anagram):
    lst = []
    for letter in anagram:
        lst.append(letter)
    return lst


counter = 0
ordinal = ['first', 'second']

print("Let's check is two words are anagrams shall we?")
user_input = input('Enter the ' + ordinal[counter] + ' word to compare: ')
anagram = is_valid(user_input)
lst_1 = sorted(string_to_list(anagram))
user_input = input('Enter the ' + ordinal[counter] + ' word to compare: ')
anagram = is_valid(user_input)
lst_2 = sorted(string_to_list(anagram))

anagram_1 = ''.join(lst_1)
anagram_2 = ''.join(lst_2)

if anagram_1 == anagram_2:
    print('They are anagrams.')
else:
    print("They aren't anagrams")


# %%
# Course solution

str_1 = input("Podaj pierwszy lancuch znakow: ")
str_2 = input("Podaj drugi lancuch znakow: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
    print("Anagrams")
else:
    print("Not anagrams")
