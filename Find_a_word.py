# %%
# Checks if the first string is hidden in second string.

ok = False
while not ok:
    searching_for = input('Enter a word, to search in next string: ').lower()
    ok = searching_for.isalpha() and len(searching_for) != 0
    if not ok:
        searching_for = input('Only words are valid. Please enter a word without'
                              ' spaces and special signs: ').lower()

ok = False
while not ok:
    base_string = input('Enter a word, to search in next string: ').lower()
    ok = base_string.isalpha() and len(base_string) != 0
    if not ok:
        base_string = input('Only words are valid. Please enter a word without'
                            ' spaces and special signs: ').lower()


if base_string.find(searching_for) >= 0:
    print('The word ' + '"' + searching_for + '"' + ' is present in given string set.')
else:
    print('The word ' + '"' + searching_for + '"' + ' is absent in given string set.')

# %%
# # Solution from PCAP LAB 5.8.1.10 Finf a word!
#
# slowo = input("Podaj slowo do wyszukania: ").upper()
# znaki = input("Podaj ciag znakow, ktory chesz przeszukac: ").upper()
#
# znalezione = True
# start = 0
#
# for lit in slowo:
#     pos = znaki.find(lit, start)
#     if pos < 0:
#         znalezione = False
#         break
#     start = pos + 1
# if znalezione:
#     print("Tak")
# else:
#     print("Nie")
