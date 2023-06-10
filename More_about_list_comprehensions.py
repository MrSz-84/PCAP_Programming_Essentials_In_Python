# %% I switched to English version of PCAP Python essentials due to lost of errors and
# deficiencies in Polish version od the course. As the result, numeration of chapters will
# varry. PCAP 4.1.4 More about list comprehensions

# list_1 = []
#
# for ex in range(6):
#     list_1.append(10 ** ex)
#
# list_2 = [10 ** ex for ex in range(6)]
#
# print(list_1)
# print(list_2)

# %% More about list comprehensions - continuation
# the_list = []
#
# for x in range(10):
#     the_list.append(1 if x % 2 == 0 else 0)
#
# print(the_list)
#
# the_list2 = [1 if x % 2 == 0 else 0 for x in range(10)]
#
# print(the_list2)

# %% More about list comprehensions - list comprehensions as generators
# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
# the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
#
# for v in the_list:
#     print(v, end=" ")
# print()
#
# for v in the_generator:
#     print(v, end=" ")
# print()
#
# print(len(the_list))
# print(len(the_generator))

# %% More about list comprehensions
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

