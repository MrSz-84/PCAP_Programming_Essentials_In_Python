# %% 4.1.5 The lambda function
# two = lambda: 2
# sqr = lambda x: x * x
# pwr = lambda x, y: x ** y
#
# for a in range(-2, 3):
#     print(sqr(a), end=" ")
#     print(pwr(a, two()))

# %% 4.1.6 How to use lambdas and what for?
# def print_function(args, fun):
#     for x in args:
#         print("f(", x, ")=", fun(x), sep="")


# def poly(x):
#     return 2 * x ** 2 - 4 * x + 2
#
#
# print_function([x for x in range(-2, 3)], poly)
#
#
# def print_function1(args, fun):
#     for x in args:
#         print("f(", x, ")=", fun(x), sep="")
#
#
# print_function1([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)

# %% 4.1.7 Lambdas and the map() function
# list_1 = [x for x in range(5)]
# list_2 = list(map(lambda x: 2 ** x, list_1))
# print(list_2)
#
# for x in map(lambda x: x * x, list_2):
#     print(x, end=" ")
# print()

# %% 4.1.8 Lambdas and the filter() function
# from random import seed, randint
#
# seed()
# data = [randint(-10, 10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
#
# print(data)
# print(filtered)

# %% 4.1.9 A brief look at closures
# def outer(par):
#     loc = par
#
#     def inner():
#         return loc
#     return inner
#
#
# var = 1
# fun = outer(var)
#
# print(fun())

# %%
# def make_closure(par):
#     loc = par
#
#     def power(p):
#         return p ** loc
#     return power
#
#
# fsqr = make_closure(2)
# fcub = make_closure(3)
#
# for i in range(5):
#     print(i, fsqr(i), fcub(i))
#
# # %%
# def tag(tg):
#     tg2 = tg
#     tg2 = tg[0] + '/' + tg[1:]
#
#     def inner(str):
#         return tg + str + tg2
#
#     return inner
#
#
# b_tag = tag('<b>')
# print(b_tag('Monty Python'))
#
# # %%
# class Vowels:
#     def __init__(self):
#         self.vow = "aeiouy "  # Yes, we know that y is not always considered a vowel.
#         self.pos = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.pos == len(self.vow):
#             raise StopIteration
#         self.pos += 1
#         return self.vow[self.pos - 1]
#
#
# vowels = Vowels()
# for v in vowels:
#     print(v, end=' ')

# %%
any_list = [1, 2, 3, 4]
even_list = list(map(lambda x: x + 1 if x % 2 == 0 else x, any_list))
print(even_list)

any_list1 = [1, 2, 3, 4]
even_list1 = list(map(lambda n: n | 1, any_list1))
print(even_list1)

# %% how to use lambdas according to PEP 8


# Recommended:
def f(x): return 3 * x


# Not recommended:
f = lambda x: 3 * x
