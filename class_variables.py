# %% properties
# class ExemplaryClass:
#     counter = 0
#
#     def __init__(self, value=1):
#         self.__first = value
#         ExemplaryClass.counter += 1
#
#
# exemplary_object1 = ExemplaryClass()
# exemplary_object2 = ExemplaryClass(2)
# exemplary_object3 = ExemplaryClass(4)
#
# print(exemplary_object1.__dict__, exemplary_object1.counter)
# print(exemplary_object2.__dict__, exemplary_object2.counter)
# print(exemplary_object3.__dict__, exemplary_object3.counter)

# %% properties continuation
# class ExemplaryClass:
#     __counter = 0
#
#     def __init__(self, value=1):
#         self.__first = value
#         ExemplaryClass.__counter += 1
#
#
# exemplary_object1 = ExemplaryClass()
# exemplary_object2 = ExemplaryClass(2)
# exemplary_object3 = ExemplaryClass(4)
#
# print(exemplary_object1.__dict__, exemplary_object1._ExemplaryClass__counter)
# print(exemplary_object2.__dict__, exemplary_object2._ExemplaryClass__counter)
# print(exemplary_object3.__dict__, exemplary_object3._ExemplaryClass__counter)


# %% class variables continuation
#
# class ExemplaryClass:
#     variable = 1
#
#     def __init__(self, value):
#         ExemplaryClass.variable = value
#
#
# print(ExemplaryClass.__dict__)
# exemplary_object = ExemplaryClass(2)
#
# print(ExemplaryClass.__dict__)
# print(exemplary_object.__dict__)

# %% does an attribute exist?
#
# class ExemplaryClass:
#     def __init__(self, value):
#         if value % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# exemplary_object = ExemplaryClass(1)
# print(exemplary_object.a)
#
# try:
#     print(exemplary_object.b)
# except AttributeError:
#     pass

# %% does an attribute exist? hasattr function
#
# class ExemplaryClass:
#     def __init__(self, value):
#         if value % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# exemplary_object = ExemplaryClass(1)
# print(exemplary_object.a)
# if hasattr(exemplary_object, 'b'):
#     print(exemplary_object.b)

# %% does a variable of a class is available to invoke? hasattr
#
# class ExemplaryClass:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#
#
# exemplary_object = ExemplaryClass()
#
# print(hasattr(exemplary_object, 'b'))
# print(hasattr(exemplary_object, 'a'))
# print(hasattr(ExemplaryClass, 'b'))
# print(hasattr(ExemplaryClass, 'a'))

# %%
#
#
# class KlasaPrzykladowa:
#     atr = 1
#
#
# print(hasattr(KlasaPrzykladowa, 'atr'))
# print(hasattr(KlasaPrzykladowa, 'prop'))

# %%

# hasattr(wersja_2, 'constrictor')

# %% super() and class name for subclasses invocation

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print('I don\'t know what I say')


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        # Pet.__init__(self, name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):
    def speak(self):
        print('Bark')


p = Pet('Tim', 19)
p.speak()
c = Cat('Bill', 34, 'Black')
c.show()
d = Dog('Jill', 25)
d.speak()
