# %% OOP 6.6.1.1 -> Four simple programs: More about exceptions
# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print('Division resulted in failure')
#         return None
#     else:
#         print('Everything went well')
#         return n
#
#
# print(reciprocal(2))
# print(reciprocal(0))

# %% OOP 6.6.1.2 -> Four simple programs: More about exceptions
# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print('Division resulted in failure')
#         n = None
#     else:
#         print('Everything went well')
#     finally:
#         print('Good bye')
#         return n
#
#
# print(reciprocal(2))
# print(reciprocal(0))

# %% OOP 6.6.1.3 -> Four simple programs: exceptions are classes
# try:
#     i = int('Halo!')
# except Exception as e:
#     print(e)
#     print(e.__str__())

# %% OOP 6.6.1.4 -> Four simple programs: exceptions are classes
# def display_tree(class_, nesting=0):
#     if nesting > 1:
#         print('   |' * (nesting - 1), end='')
#     if nesting > 0:
#         print('   +---', end='')
#
#     print(class_.__name__)
#
#     for subclass in class_.__subclasses__():
#         display_tree(subclass, nesting + 1)
#
#
# display_tree(BaseException)

# %% OOP 6.6.1.5 -> Four simple programs: exceptions anatomy
# def print_args(args):
#     lng = len(args)
#     if lng == 0:
#         print('')
#     elif lng == 1:
#         print(args[0])
#     else:
#         print(str(args))
#
#
# try:
#     raise Exception
# except Exception as e:
#     print(e, e.__str__(), sep=' : ', end=' : ')
#     print_args(e.args)
#
# try:
#     raise Exception('my exception')
# except Exception as e:
#     print(e, e.__str__(), sep=' : ', end=' : ')
#     print_args(e.args)
#
# try:
#     raise Exception('my', 'exception')
# except Exception as e:
#     print(e, e.__str__(), sep=' : ', end=' : ')
#     print_args(e.args)

# %% OOP 6.6.1.6 -> Four simple programs: how to create your own exception
# class MyZeroDivisionError(ZeroDivisionError):
#     pass
#
#
# def divide(my):
#     if my:
#         raise MyZeroDivisionError('Terrible news')
#     else:
#         raise ZeroDivisionError('Bad news')
#
#
# for mode in [False, True]:
#     try:
#         divide(mode)
#     except ZeroDivisionError:
#         print('Division by zero')
#
# for mode in [False, True]:
#     try:
#         divide(mode)
#     except MyZeroDivisionError:
#         print('My division by zero')
#     except ZeroDivisionError:
#         print('Ordinary division by zero')

# %% OOP 6.6.1.7 -> Four simple programs: how to create your own exception - continuation
# class PizzaError(Exception):
#     def __init__(self, pizza, message):
#         super().__init__(message)
#         self.pizza = pizza
#
#
# class TooMuchCheeseError(PizzaError):
#     def __init__(self, pizza, cheese, message):
#         super().__init__(pizza, message)
#         self.cheese = cheese


# %% OOP 6.6.1.8 -> Four simple programs: how to create your own exception - follow up
# class PizzaError(Exception):
#     def __init__(self, pizza, message):
#         super().__init__(message)
#         self.pizza = pizza
#
#
# class TooMuchCheeseError(PizzaError):
#     def __init__(self, pizza, cheese, message):
#         super().__init__(pizza, message)
#         self.cheese = cheese
#
#
# def make_pizza(pizza, cheese):
#     if pizza not in ['margherita', 'capricciosa', 'calzone']:
#         raise PizzaError(pizza, 'Chosen pizza not in the menu')
#     if cheese > 100:
#         raise TooMuchCheeseError(pizza, cheese, 'Too much cheese')
#     print('Pizza ready!')
#
#
# for (pizz, chee) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
#     try:
#         make_pizza(pizz, chee)
#     except TooMuchCheeseError as tmce:
#         print(tmce, ':', tmce.cheese)
#     except PizzaError as pe:
#         print(pe, ':', pe.pizza)

# %% OOP 6.6.1.8 -> Four simple programs: how to create your own exception - follow up
class PizzaError(Exception):
    def __init__(self, pizza='unknown', message=''):
        super().__init__(message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='unknown', cheese='>100', message=''):
        super().__init__(pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print('Pizza ready!')


for (pizz, chee) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pizz, chee)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

# %% OOP 6.6.1.9 -> Four simple programs: summary
try:
    assert __name__ == "__main__"
except:
    print("porazka", end=' ')
else:
    print("sukces", end=' ')
finally:
    print("koniec")

import math

try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("dobrze")

import math

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("dobrze")
finally:
    print("koniec")

import math

class NewValueError(ValueError):
    def __init__(self, nazwa, kolor, stan):
        self.data = (nazwa, kolor, stan)

try:
    raise NewValueError("Ostrzeżenie przed wrogiem","Czerwony alarm","Najwyższa gotowość")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')