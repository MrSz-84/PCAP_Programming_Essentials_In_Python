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
# properties and methods: continuation
class Lvl1:
    variable_1 = 100

    def __init__(self) -> None:
        self.var_1 = 101

    def fun_1(self):
        return 102


class Lvl2(Lvl1):
    variable_2 = 200

    def __init__(self) -> None:
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202


class Lvl3(Lvl2):
    variable_3 = 300

    def __init__(self) -> None:
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Lvl3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
