# %%
# Przyklad 1

slowo = 'by'
print(len(slowo))


# Przyklad 2

pusty = ''
print(len(pusty))


# Przyklad 3

i_am = 'I\'m'
print(len(i_am))

# %%
multiLine = '''Line #1 
Linia #2'''

print(len(multiLine))

# %%
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# %%
# Przedstawienie funkcji ord()

char_1 = 'a'
char_2 = ' '  # spacja

print(ord(char_1))
print(ord(char_2))

# %%
# Przedstawienie funkcji chr()

print(chr(97))
print(chr(945))

# %%
# Indeksowanie łańcuchów znaków

przykladowy_lancuch = 'głupie kroki'

for ix in range(len(przykladowy_lancuch)):
    print(przykladowy_lancuch[ix], end=' ')

print()

# Iteracja za pomoca łańcucha znakow

przykladowy_lancuch = 'głupie kroki'

for ch in przykladowy_lancuch:
    print(ch, end=' ')

print()

# %%
# Wycinki

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# %%
# operator in and not in
alfabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alfabet)
print("F" in alfabet)
print("1" in alfabet)
print("ghi" in alfabet)
print("Xyz" in alfabet)

alfabet = "abcdefghijklmnopqrstuvwxyz" 

print("f" not in alfabet) 
print("F" not in alfabet) 
print("1" not in alfabet) 
print("ghi" not in alfabet) 
print("Xyz" not in alfabet)

# %%
alfabet = "bcdefghijklmnopqrstuvwxy"

alfabet = "a" + alfabet
alfabet = alfabet + "z"

print(alfabet)

# %%
# Przedstawienie min() - Przyklad 1
print(min("aAbByYzZ"))


# Przedstawienie min() - Przyklady 2 i 3
t = 'Rycerze, ktorzy mowia "Nie!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# %%
# Przedstawienie max() - Przyklad 1
print(max("aAbByYzZ"))


# Przedstawienie max() - Przyklady 2 i 3
t = 'Rycerze, ktorzy mowia "Nie!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# %%
# Przedstawienie metody index()
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# %%
# Przedstawienie funkcji list()
print(list("abcabc"))

# Przedstawienie metody count()
print("abcabc".count("b"))
print('abcabc'.count("d"))

# %%
s1 = 'Gdzie są niegdysiejsze śniegi?'
s2 = s1.split()
print(s2)
print(s2[-2])