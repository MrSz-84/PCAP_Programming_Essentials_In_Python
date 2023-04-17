def l100kmtompg(litry):
    return (100 / 1.609344) / (litry / 3.785411784)
    


def mpgtol100km(mile):
    return (3.785411784 / (mile * 1.609344) * 100)


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))