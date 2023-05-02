# %% 6.5.1.1 OOP -> Inheritance - how and why?
# class Star:
#     def __init__(self, name, galactic):
#         self.name = name
#         self.galactic = galactic


# sun = Star('Sun', 'Milky Way')
# print(sun)

# %% 6.5.1.2 OOP -> Inheritance - how and why?
# class Star:
#     def __init__(self, name, galactic) -> None:
#         self.name = name
#         self. galactic = galactic

#     def __str__(self) -> str:
#         return self.name + ' in ' + self.galactic


# sun = Star('Sun', 'Milky Way')
# print(sun)

# %% 6.5.1.3 OOP -> Inheritance - how and why?
# class Vehicles:
#     pass


# class LandVehicles(Vehicles):
#     pass


# class TrackedVehicles(LandVehicles):
#     pass

# %% 6.5.1.4 OOP -> Inheritance - issubclass()
# class Vehicles:
#     pass


# class LandVehicles(Vehicles):
#     pass


# class TrackedVehicles(LandVehicles):
#     pass


# for cls1 in [Vehicles, LandVehicles, TrackedVehicles]:
#     for cls2 in [Vehicles, LandVehicles, TrackedVehicles]:
#         print(issubclass(cls1, cls2), end='\t')

# %% 6.5.1.5 OOP -> Inheritance - isinstance()
# class Vehicles:
#     pass


# class LandVehicles(Vehicles):
#     pass


# class TrackedVehicles(LandVehicles):
#     pass


# my_vehicle = Vehicles()
# my_land_vehicle = LandVehicles()
# my_track_vehicle = TrackedVehicles()


# for obj in [my_vehicle, my_land_vehicle, my_track_vehicle]:
#     for cls in [Vehicles, LandVehicles, TrackedVehicles]:
#         print(isinstance(obj, cls), end='\t')

# %% 6.5.1.6 OOP -> Inheritance - is operand
# class ExemplaryClass:
#     def __init__(self, val) -> None:
#         self.val = val


# ob_1 = ExemplaryClass(0)
# ob_2 = ExemplaryClass(2)
# ob_3 = ob_1
# ob_3.val += 1

# print(ob_1 is ob_2)
# print(ob_2 is ob_3)
# print(ob_3 is ob_1)
# print(ob_1.val, ob_2.val, ob_3.val)

# str_1 = 'Ala ma '
# str_2 = 'Ala ma kota'
# str_1 += 'kota'

# print(str_1 == str_2, str_1 is str_2)

# %% 6.5.1.7 OOP -> Inheritance - how Python language finds
# properties and methods
# class Super:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __str__(self) -> str:
#         return 'My name is ' + self.name + '.'


# class Sub(Super):
#     def __init__(self, name) -> None:
#         super().__init__(name)


# obj = Sub('Adam')

# print(obj)

# %% 6.5.1.8 OOP -> Inheritance - how Python language finds
# properties and methods: continuation
# class Super:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __str__(self) -> str:
#         return 'My name is ' + self.name + '.'


# class Sub(Super):
#     def __init__(self, name) -> None:
#         super().__init__(name)


# obj = Sub('Adam')

# print(obj)

# %% 6.5.1.9 OOP -> Inheritance - how Python language finds
# properties and methods: continuation
# class Super:
#     variableSup = 1


# class Sub(Super):
#     variableSub = 2


# obj = Sub()

# print(obj.variableSub)
# print(obj.variableSup)

# %% 6.5.1.10 OOP -> Inheritance - how Python language finds
# properties and methods: continuation
# class Super:
#     def __init__(self) -> None:
#         self.variableSup = 11


# class Sub(Super):
#     def __init__(self) -> None:
#         super().__init__()
#         self.variableSub = 12


# obj = Sub()

# print(obj.variableSub)
# print(obj.variableSup)

# %% 6.5.1.11 OOP -> Inheritance - how Python language finds
# properties and methods: continuation.
# class Lvl1:
#     variable_1 = 100

#     def __init__(self) -> None:
#         self.var_1 = 101

#     def fun_1(self):
#         return 102


# class Lvl2(Lvl1):
#     variable_2 = 200

#     def __init__(self) -> None:
#         super().__init__()
#         self.var_2 = 201

#     def fun_2(self):
#         return 202


# class Lvl3(Lvl2):
#     variable_3 = 300

#     def __init__(self) -> None:
#         super().__init__()
#         self.var_3 = 301

#     def fun_3(self):
#         return 302


# obj = Lvl3()

# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())

# %% 6.5.1.12 OOP -> Inheritance - how Python language finds
# # properties and methods: continuation - multiple super classes
#  SuperA:
#     var_A = 10

#     def fun_A(self):
#         return 11


# class SuperB:
#     var_B = 20

#     def fun_B(self):
#         return 21


# class Sub(SuperA, SuperB):
#     pass


# obj = Sub()

# print(obj.var_A, obj.fun_A())
# print(obj.var_B, obj.fun_B())

# %% 6.5.1.13 OOP -> Inheritance - how Python language finds
# properties and methods: continuation - inheritance the same function name
# or property name.
# class Lvl1:
#     var = 100

#     def fun(self):
#         return 101


# class Lvl2:
#     var = 200

#     def fun(self):
#         return 201


# class Lvl3(Lvl2):
#     pass


# obj = Lvl3()

# print(obj.var, obj.fun())

# %% 6.5.1.14 OOP -> Inheritance - how Python language finds
# properties and methods: continuation - inheritance the same function name
# or property name from multiple super classes.
# class Left:
#     var = 'L'
#     var_left = 'LL'

#     def fun(self):
#         return 'Left'


# class Right:
#     var = 'R'
#     var_right = 'RR'

#     def fun(self):
#         return 'Right'


# class Sub(Right, Left):
#     pass


# obj = Sub()

# print(obj.var, obj.var_left, obj.var_right, obj.fun())

# %% 6.5.1.15 OOP -> Inheritance - how to create class hierarchy
# class One:
#     def do_it(self):
#         print('do_it from One')

#     def doanything(self):
#         self.do_it()


# class Two(One):
#     def do_it(self):
#         print('do_it from Two')


# one = One()
# two = Two()

# one.doanything()
# two.doanything()

# %% 6.5.1.16 OOP -> Inheritance - how to create class hierarchy: continuation
# import time


# class TrackedVehicles:
#     def tracks_control(left, stop):
#         pass

#     def turn(left):
#         tracks_control(left, True)
#         time.sleep(0.25)
#         tracks_control(left, False)


# class WheelVehicles:
#     def turn_front_wheels(left, on):
#         pass

#     def turn(left):
#         turn_front_wheels(left, True)
#         time.sleep(0.25)
#         turn_front_wheels(left, False)

# %% 6.5.1.17 OOP -> Inheritance - how to create class hierarchy: continuation
# import time


# class Vehicles:

#     def change_direction(left, on):
#         pass

#     def turn(left):
#         change_direction(left, True)
#         time.sleep(0.25)
#         change_direction(left, False)


# class TrackedVehicles(Vehicles):
#     def tracks_control(left, stop):
#         pass

#     def change_direction(left, on):
#         tracks_control(left, on)


# class WheeledVehicles(Vehicles):
#     def turn_front_wheels(left, on):
#         pass

#     def change_direction(left, on):
#         turn_front_wheels(left, on)

# %% 6.5.1.18 OOP -> Inheritance - how to create class hierarchy: continuation
# import time


# class TrackedVehicles():
#     def change_direction(self, left, on):
#         print('tracks: ', left, on)


# class WheeledVehicles():
#     def change_direction(self, left, on):
#         print('wheels: ', left, on)


# class Vehicles:
#     def __init__(self, controller) -> None:
#         self.controller = controller

#     def turn(self, left):
#         self.controller.change_direction(left, True)
#         time.sleep(0.25)
#         self.controller.change_direction(left, False)


# wheeled = Vehicles(WheeledVehicles())
# tracked = Vehicles(TrackedVehicles())

# wheeled.turn(True)
# tracked.turn(False)

# %% 6.5.1.20 OOP -> Inheritance - key issues
class Mouse:
    def __init__(self, name):
        self.my_name = name

    def __str__(self):
        return self.my_name


the_mouse = Mouse('mickey')
print(the_mouse)  # Daje na wyjściu "mickey".


# %%
class Mouse:
    pass


class LabMouse(Mouse):
    pass


print(issubclass(Mouse, LabMouse), issubclass(
    LabMouse, Mouse))  # Daje na wyjściu "False True"


# %%
class Mouse:
    pass


class LabMouse(Mouse):
    pass


mickey = Mouse()
# Daje na wyjściu "True False".
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))


# %%
class Mouse:
    pass


mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
# Daje na wyjściu "False True".
print(mickey is minnie, mickey is cloned_mickey)


# %%
class Mouse:
    def __str__(self):
        return "Mouse"


class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()


doctor_mouse = LabMouse()
print(doctor_mouse)  # Prints "Laboratory Mouse".


# %%
class Mouse:
    Population = 0

    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hi, my name is " + self.name


class LabMouse(Mouse):
    pass


professor_mouse = LabMouse("Professor Mouser")
# Prints "Hi, my name is Professor Mouser 1"
print(professor_mouse, Mouse.Population)


# %%
class Mouse:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name


class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name


mus = AncientMouse("Caesar")  # Prints "Meum nomen est Caesar"
print(mus)


# %% 6.5.1.21 OOP -> Inheritance - exercises
class Dog:
    kennel = 0

    def __init__(self, breed) -> None:
        self.breed = breed
        Dog.kennel += 1

    def __str__(self) -> str:
        return self.breed + ' says: Woof!'


class SheepDog(Dog):
    def __str__(self) -> str:
        return super().__str__() + ' Don\'t run little sheep!'


class LowlandDog(SheepDog):
    def __str__(self) -> str:
        return Dog.__str__(self) + ' I don\'t like mountains!'


class GuardDog(Dog):
    def __str__(self) -> str:
        return super().__str__() + ' Stay where you are mister trespasser!'


rocky = SheepDog('Collie')
luna = GuardDog('Doberman')
erwin = LowlandDog('Valee Sheepdog')

print(rocky)
print(luna)
print(erwin)

print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))

print(luna is luna, rocky is luna)
print(rocky.kennel)
