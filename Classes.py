# %% class defining
# class SimplestClass:
#     pass
#
# my_first_object = SimplestClass

# # %% stack LIFO using procedural approach
# def push(val):
#     stack.append(val)
#
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
#
# stack = []
#
# for w in range(3, 0, -1):
#     push(w)
#
# for r in range(3):
#     print(pop())

# # %% stack LIFO using object-orientated approach
#
# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#
# object_stack = Stack()
#
# for w in range(3, 0, -1):
#     object_stack.push(w)
#
# for r in range(3):
#     print(object_stack.pop())

# %% multiple LIFO stack using same class/method

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


object_stack = Stack()
object_stack2 = Stack()

object_stack.push(3)
object_stack2.push(object_stack.pop())

print(object_stack2.pop())

