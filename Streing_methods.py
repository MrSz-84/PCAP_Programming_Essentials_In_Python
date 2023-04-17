# %%
# Przedstawienie metody capitalize()
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# %%
# Przedstawienie metody center()
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center
            (20, '*') + ']')

# %%
# Przedstawienie metody endswith()
if "epsilon".endswith("on"):
    print("tak")
else:
    print("nie")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# %%
# Przedstawienie metody find()
print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print('kappa'.find('a', 2))

txt = """Odmiana zwyklego tekstu lorem ipsum
byla uzywana w druku od lat szescdziesiatych 
lub wczesniej, kiedy zostala spopularyzowany przez reklamy 
arkuszy transferowych Letraset. Zostala wprowadzony 
do Ery Informatyzacji w polowie lat osiemdziesiatych XX wieku przez Aldus Corporation, 
firme ktora wykorzystała ja w szablonach graficznych i edytorach tekstu
w swoim programie do publikowania PageMaker (z Wikipedii)"""

fnd = txt.find("do")
while fnd != -1:
    print(fnd)
    fnd = txt.find("do", fnd + 1)

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

# %%
# Przedstawienie metody isalnum()
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

# %%
# Przykład 1: Przedstawienie metody isalpha()
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Przykład 2: Przedstawienie metody isdigit()
print('2018'.isdigit())
print("Year2019".isdigit())

# %%
# Przykład 1: Przedstawienie metody islower()
print("Moooo".islower())
print('moooo'.islower())

# Przykład 2: Przedstawienie metody isspace()
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Przykład 3: Przedstawienie metody isupper()
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# %%
# Przedstawienie metody join()
print(", ".join(["omicron", "pi", "rho"]))

# %%
# Przedstawienie metody lower()
print("SiGmA=60".lower())

# Przedstawienie metody upper()
print("SiGmA=60".upper())

# %%
# Przedstawienie metody lstrip()
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

# %%
# Przedstawienie metody replace()
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("To jest to!".replace("jest", "sa"))
print("Sok jablkowy".replace("jablkowy", ""))
print("To jest to!".replace("jest", "sa", 1))
print("To jest to!".replace("jest", "sa", 2))

# %%
# Przedstawienie metody rfind()
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# %%
# Przedstawienie metody rstrip()
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
t = "cisco.com".rstrip("com")
t = t.rstrip(".")
print(t)

# %%
# Przedstawienie metody split()
print("phi       chi\npsi".split())
t = "phi       chi\npsi".split()
t = " ".join(t)
print(t)

# %%

# Przedstawienie metody startswith()
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# Przedstawienie metody strip()
print("[" + "   aleph   ".strip() + "]")

# %%
# Przedstawienie metody swapcase()
print("Wiem, ze nic nie wiem.".swapcase())

print()

# Przedstawienie metody title()
print("Wiem, ze nic nie wiem. Czesc 1.".title())

print()

# Przedstawienie metody upper()
print("Wiem, ze nic nie wiem. Czesc 2.".upper())
