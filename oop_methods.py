# %% OOP Methods 6.4.1.1 -> Methods in details
# class Classy:
#     def method(self, par):
#         print('method:', par)


# obj = Classy()
# obj.method(1)
# obj.method(2)
# obj.method(3)

# %% OOP Methods 6.4.1.2 -> Methods in details: continuation
# class Classy:
#     var = 2

#     def method(self):
#         print(self.var, self.variable)


# obj = Classy()
# obj.variable = 3
# obj.method()

# %% OOP Methods 6.4.1.2 -> Methods in details: continuation
# class Classy:
#     def another(self):
#         print('another')

#     def method(self):
#         print('method')
#         self.another()


# obj = Classy()
# obj.method()

# %% OOP Methods 6.4.1.3 -> Methods in details: continuation
# class Classy:
#     def __init__(self, val) -> None:
#         self.var = val


# obj_1 = Classy('object')
# print(obj_1.var)

# %% OOP Methods 6.4.1.4 -> Methods in details: continuation
# class Classy:
#     def __init__(self, val=None):
#         self.val = val


# obj1 = Classy('object')
# obj2 = Classy()

# print(obj1.val)
# print(obj2.val)

# %% OOP Methods 6.4.1.4 -> Methods in details: continuation
# class Classy:
#     def visable(self):
#         print('visable')

#     def __hidden(self):
#         print('hidden')


# obj = Classy()
# obj.visable()

# try:
#     obj.__hidden()
# except:
#     print('failure')

# obj._Classy__hidden()

# %% OOP Methods 6.4.1.5 -> Inner life of classes and objects
# class Classy:
#     var = 1

#     def __init__(self):
#         self.var = 2

#     def method(self):
#         pass

#     def __hidden(self):
#         pass


# obj = Classy()

# print(obj.__dict__)
# print(Classy.__dict__)

# %% OOP Methods 6.4.1.6 -> Inner life of classes and objects: continuation
# class Classy:
#     pass


# print(Classy.__name__)
# obj = Classy()
# print(type(obj).__name__)

# %% OOP Methods 6.4.1.7 -> Inner life of classes and objects: continuation
# class Classy:
#     pass


# print(Classy.__module__)
# obj = Classy()
# print(obj.__module__)

# %% OOP Methods 6.4.1.8 -> Inner life of classes and objects: continuation
# class SuperOne:
#     pass


# class SuperTwo:
#     pass


# class Sub(SuperOne, SuperTwo):
#     pass


# def print_bases(cls):
#     print('( ', end='')

#     for x in cls.__bases__:
#         print(x.__name__, end=' ')
#     print(')')


# print_bases(SuperOne)
# print_bases(SuperTwo)
# print_bases(Sub)


# print(SuperOne.__bases__)
# print(SuperTwo.__bases__)
# print(Sub.__bases__)

# %% OOP Methods 6.4.1.10 -> Classes exploration
# class MyClass:
#     pass


# obj = MyClass()
# obj.a = 1
# obj.b = 2
# obj.i = 3
# obj.ireal = 3.5
# obj.integer = 4
# obj.z = 5


# def incIntsI(obj):
#     for name in obj.__dict__.keys():
#         if name.startswith('i'):
#             val = getattr(obj, name)
#             if isinstance(val, int):
#                 setattr(obj, name, val + 1)


# print(obj.__dict__)
# incIntsI(obj)
# print(obj.__dict__)

# %% OOP Methods 6.4.1.11 -> Summary
# class Example:
#     def __init__(self):
#         self.name = Example.__name__

#     def myself(self):
#         print("My name is " + self.name + " and I live in " + Example.__module__)


# obj = Example()
# obj.myself()


class Snake:
    def __init__(self, victims):
        self.victims = victims

    def increase(self):
        self.victims += 1


obj = Snake(12)
print(obj.victims)
obj.increase()
print(obj.victims)
