# # %% exemplary class
#
# class ExemplaryClass:
#     def __init__(self, value=1):
#         self.first = value
#
#     def set_second(self, value):
#         self.second = value
#
#
# exemplary_object1 = ExemplaryClass()
# exemplary_object2 = ExemplaryClass(2)
#
# exemplary_object2.set_second(3)
#
# exemplary_object3 = ExemplaryClass(4)
# exemplary_object3.third = 5
#
# print(exemplary_object1.__dict__)
# print(exemplary_object2.__dict__)
# print(exemplary_object3.__dict__)


# %% Making properties private

class ExemplaryClass:
    def __init__(self, value=1):
        self.__first = value

    def set_second(self, value):
        self.__second = value


exemplary_object1 = ExemplaryClass()
exemplary_object2 = ExemplaryClass(2)

exemplary_object2.set_second(3)

exemplary_object3 = ExemplaryClass(4)
exemplary_object3.__third = 5

print(exemplary_object1.__dict__)
print(exemplary_object2.__dict__)
print(exemplary_object3.__dict__)

print(exemplary_object1._ExemplaryClass__first)
