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

# # %% multiple LIFO stack using same class/method
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
# object_stack2 = Stack()
#
# object_stack.push(3)
# object_stack2.push(object_stack.pop())
#
# print(object_stack2.pop())

# %% a subclass for all stacks sum evaluation support
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
# class StackAdd(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
#
#     def get_sum(self):
#         return self.__sum
#
#
# stack_object = StackAdd()
#
# for i in range(5, 0, -1):
#     stack_object.push(i)
# print(stack_object.get_sum())
#
# for i in range(5):
#     print(stack_object.pop())
#

# %% LAB counting stack
#
# class Stack:
#     def __init__(self):
#         self.__stk = []
#
#     def push(self, val):
#         self.__stk.append(val)
#
#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val
#
#
# class CountingStack(Stack):
#     def __init__(self):
#         super().__init__()
#         self.__pop_sum = 0
#
#     def get_counter(self):
#         return self.__pop_sum
#
#     def pop(self):
#         self.__pop_sum += 1
#         return super().pop()
#
#
# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())

# %% Queue aka FIFO
#
# class QueueError(Exception):
#     pass
#
#
# class Queue:
#     def __init__(self):
#         self.__stack = []
#
#     def put(self, element):
#         self.__stack.insert(0, element)
#
#     def get(self):
#         if len(self.__stack) < 1:
#             raise QueueError
#         else:
#             val = self.__stack[-1]
#             del self.__stack[-1]
#             return val
#
#
# que = Queue()
# que.put(1)
# que.put("dog")
# que.put(False)
# try:
#     for i in range(4):
#         print(que.get())
# except:
#     print("Queue error")


# %% Queue aka FIFO part 2

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.stack = []

    def put(self, element):
        self.stack.insert(0, element)

    def get(self):
        if len(self.stack) < 1:
            raise QueueError
        else:
            val = self.stack[-1]
            del self.stack[-1]
            return val


class SuperQueue(Queue):
    def isempty(self):
        return len(self.stack) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
