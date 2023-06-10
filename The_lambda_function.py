# %% 4.1.5 The lambda function
# two = lambda: 2
# sqr = lambda x: x * x
# pwr = lambda x, y: x ** y
#
# for a in range(-2, 3):
#     print(sqr(a), end=" ")
#     print(pwr(a, two()))

# %% 4.1.6 How to use lambdas and what for?
def print_function(args, fun):
    for x in args:
        print("f(", x, ")=", fun(x), sep="")


def poly(x):
    return 2 * x ** 2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)


def print_function1(args, fun):
    for x in args:
        print("f(", x, ")=", fun(x), sep="")


print_function1([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)

# %% 4.1.7 Lambdas and the map() function
