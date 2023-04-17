from sys import path
from PyCharm.Modules.dirmod.module import suml, prodl


path.insert(0, '..\\packages')


import sys

for p in sys.path:
    print(p)


zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

# %%