# %% OOP 6.7.1.2 Generators and closures -> Generators where to find them: continuation
# class Fib:
#     def __init__(self, nn):
#         print('__init__')
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print('__iter__')
#         return self
#
#     def __next__(self):
#         print('__next__')
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
#
# for i in Fib(10):
#     print(i)

# %% OOP 6.7.1.3 Generators and closures -> Generators where to find them: continuation
# class Fib:
#     def __init__(self, nn):
#         self.__n = nn
#         self.__i = 0
#         self.__p1 = self.__p2 = 1
#
#     def __iter__(self):
#         print('Fib iter')
#         return self
#
#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         ret = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, ret
#         return ret
#
#
# class Class:
#     def __init__(self, n):
#         self.__iter = Fib(n)
#
#     def __iter__(self):
#         print('Class iter')
#         return self.__iter
#
#
# object = Class(8)
#
# for i in object:
#     print(i)

# %% OOP 6.7.1.4 Generators and closures -> yield instruction
# %% The yield statement
# def fun(n):
#     for i in range(n):
#         yield i

# %% how to bild a generator
# def fun(n):
#     for i in range(n):
#         yield i
#
#
# for v in fun(5):
#     print(v)

# %%
# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2
#
#
# for v in powers_of_2(8):
#     print(v)


# %% generators within list comprehensions
# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2
#
#
# t = [x for x in powers_of_2(5)]
# print(t)

# %% Transforming a series of subsequent results into a list
# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2
#
#
# t = list(powers_of_2(3))
# print(t)

# %% generators and "in" operator
# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2
#
#
# for i in range(20):
#     if i in powers_of_2(4):
#         print(i)

# %% The Fibonacci number generator
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n


fibs = list(fibonacci(10))
print(fibs)