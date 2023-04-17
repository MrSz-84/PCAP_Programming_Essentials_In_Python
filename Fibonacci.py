# First code

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
    
#     elem_1 = elem_2 = 1
#     suma = 0
#     for i in range(3, n + 1):
#         suma = elem_1 + elem_2
#         elem_1 = elem_2
#         elem_2 = suma
#     return suma

# for n in range(1, 10): # test
#     print(n, "->", fib(n))

# Code optimalisation

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
    
#     elem_1 = elem_2 = 1
#     suma = 0
#     for i in range(3, n + 1):
#         suma = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, suma
#     return suma

# for n in range(1, 10): # test
#     print(n, "->", fib(n))

# Recursion

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(1, 10):
    print(n, "->", fib(n))


