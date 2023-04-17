# # %%
# # Cezar's cypher
# txt = input("Enter a message: ")
# cypher = ''
# for char in txt:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + 1
#     if code > ord('Z'):
#         code = ord('A')
#     cypher += chr(code)
#
# print(cypher)

# %%
# Cezar's cypher - decoding the message
# cypher = input('Enter the coded message: ')
# txt = ''
# for char in cypher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     txt += chr(code)
#
# print(txt)

# # %%
# # Cezar's cypher with code value grater than one
# offset = int(input('Enter a whole number: '))
# txt = input("Enter a message: ")
# cypher = ''
# for char in txt:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + offset
#     while code > 90:
#         if code > ord('Z'):
#             code = ord('A') + (code - 90)
#     cypher += chr(code)
#
# print(cypher)

# %%
# Cezar's cypher - decoding the message with offset
# offset = int(input('Enter a whole number: '))
# cypher = input('Enter the coded message: ')
# txt = ''
# for char in cypher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - offset
#     while code < 65:
#         if code < ord('A'):
#             code = ord('Z') + (code - 65)
#     txt += chr(code)
#
# print(txt)

# %%
# Program Przetwarzajacy Liczby

# sequense = input("Enter a sequence consisting only numbers - separate them with spaces: ")
# strings = sequense.split()
# total = 0
# try:
#     for substr in strings:
#         total += float(substr)
#     print("Suma wynosi:", total)
# except:
#     print(substr, "This is not a number.")


# %%
# IBAN validator

iban_length_by_country = {'AL': 28, 'AD': 24, 'AT': 20, 'AZ': 28, 'BH': 22,
                          'BY': 28, 'BE': 16, 'BA': 20, 'BR': 29, 'BG': 22,
                          'CR': 22, 'HR': 21, 'CY': 28, 'CZ': 24, 'DK': 18,
                          'DO': 28, 'TL': 23, 'EG': 29, 'SV': 28, 'EE': 20,
                          'FO': 18, 'FI': 18, 'FR': 27, 'GE': 22, 'DE': 22,
                          'GI': 23, 'GR': 27, 'GL': 18, 'GT': 28, 'HU': 28,
                          'IS': 26, 'IQ': 23, 'IE': 22, 'IL': 23, 'IT': 27,
                          'JO': 30, 'KZ': 20, 'XK': 20, 'KW': 30, 'LV': 21,
                          'LB': 28, 'LY': 25, 'LI': 21, 'LT': 20, 'LU': 20,
                          'MK': 19, 'MT': 31, 'MR': 27, 'MU': 30, 'MC': 27,
                          'MD': 24, 'ME': 22, 'NL': 18, 'NO': 15, 'PK': 24,
                          'PS': 29, 'PL': 28, 'PT': 25, 'QA': 29, 'RO': 24,
                          'RU': 33, 'LC': 32, 'SM': 27, 'ST': 25, 'SA': 24,
                          'RS': 22, 'SC': 31, 'SK': 24, 'SI': 19, 'ES': 24,
                          'SD': 18, 'SE': 24, 'CH': 21, 'TN': 24, 'TR': 26,
                          'UA': 29, 'AE': 23, 'GB': 22, 'VA': 22, 'VG': 24}

iban = input("Type in IBAN number: ")
iban = iban.replace(' ', '')
check_prefix = 0

if len(iban) != iban_length_by_country[(iban[0:2]).upper()]:
    print('IBAN length for your country is not right.')
elif not iban.isalnum():
    print("Forbidden characters were inputted.")
elif len(iban) < 15:
    print("Entered IBAN number is to short")
elif len(iban) > 31:
    print("Entered IBAN number is to long")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("IBAN number is valid")
    else:
        print("IBAN number is invalid.")


# # %%
# # snake written by chat GPT 3.5
# import pygame
# import sys
# import random
#
# # Constants
# WIDTH = 400
# HEIGHT = 400
# GRID_SIZE = 20
# GRID_WIDTH = WIDTH // GRID_SIZE
# GRID_HEIGHT = HEIGHT // GRID_SIZE
# SNAKE_COLOR = (0, 255, 0)
# FRUIT_COLOR = (255, 0, 0)
#
# # Initialize Pygame
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Snake Game")
#
# # Initialize game state
# snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
# snake_dir = (0, 0)
# fruit = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
#
# # Game loop
# clock = pygame.time.Clock()
# target_fps = 10
#
# while True:
#     clock.tick(target_fps)  # Limit frame rate to target_fps
#
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 snake_dir = (0, -1)
#             elif event.key == pygame.K_DOWN:
#                 snake_dir = (0, 1)
#             elif event.key == pygame.K_LEFT:
#                 snake_dir = (-1, 0)
#             elif event.key == pygame.K_RIGHT:
#                 snake_dir = (1, 0)
#
#     # Update snake position
#     head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
#     snake.insert(0, head)
#
#     # Check for collision with fruit
#     if snake[0] == fruit:
#         fruit = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
#     else:
#         snake.pop()
#
#     # Check for collision with walls
#     if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
#         pygame.quit()
#         sys.exit()
#
#     # Check for collision with self
#     if head in snake[1:]:
#         pygame.quit()
#         sys.exit()
#
#     # Clear screen
#     screen.fill((0, 0, 0))
#
#     # Draw snake
#     for segment in snake:
#         pygame.draw.rect(screen, SNAKE_COLOR, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
#
#     # Draw fruit
#     pygame.draw.rect(screen, FRUIT_COLOR, (fruit[0] * GRID_SIZE, fruit[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
#
#     # Update display
#     pygame.display.flip()
