cubed = [num ** 3 for num in range(5)]
print(cubed)  # daje na wyjsciu: [0, 1, 8, 27, 64]


# Czterokolumnowa/czterorzedowa tablica - dwuwymiarowe tablice (4x4)

tablica = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(tablica)
print(tablica[0][0]) # daje na wyjściu: ':('
print(tablica[0][3]) # daje na wyjściu: ':)'


# Kostka - trójwymiarowa tablica (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0]) # daje na wyjsciu: ':('
print(cube[2][2][0]) # daje na wyjsciu: ':)'
