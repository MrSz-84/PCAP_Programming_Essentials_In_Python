# %%
# Przykłady testowe
print('alpha' == 'alpha')
print('alpha' != 'Alpha')
print('alpha' < 'alphabet')
print('beta' > 'Beta')

# %%
# Przykłady testowe
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')

# %%
print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' == 1)
print('10' > 10)

# %%
# Przedstawienie działania funkcji sorted()
greka_jeden = ['omega', 'alpha', 'pi', 'gamma']
greka_jeden_2 = sorted(greka_jeden)

print(greka_jeden)
print(greka_jeden_2)

print()

# Przedstawienie dzialania metody sort()
greka_dwa = ['omega', 'alpha', 'pi', 'gamma']
print(greka_dwa)

greka_dwa.sort()
print(greka_dwa)

# %%
# Kod testowy
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)

# %%
s1 = 'Gdzie są niegdysiejsze śniegi?'
s2 = s1.split()
s3 = sorted(s2)
print(s3)
print(s3[1])

# %%
s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)