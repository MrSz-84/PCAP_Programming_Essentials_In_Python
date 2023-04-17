# patterns = [
#     ['###', '# #', '# #', '# #', '###'],    # 0
#     ['  #', '  #', '  #', '  #', '  #'],    # 1
#     ['###', '  #', '###', '#  ', '###'],    # 2
#     ['###', '  #', '###', '  #', '###'],    # 3
#     ['# #', '# #', '###', '  #', '  #'],    # 4
#     ['###', '#  ', '###', '  #', '###'],    # 5
#     ['###', '#  ', '###', '# #', '###'],    # 6
#     ['###', '  #', '  #', '  #', '  #'],    # 7
#     ['###', '# #', '###', '# #', '###'],    # 8
#     ['###', '# #', '###', '  #', '###']     # 9
#     ]
#
#
# def led_display(user_input):
#     led_memory = [''] * 5
#     for digit in user_input:
#         memory_feed = patterns[int(digit)]
#         for col in range(len(led_memory)):
#             led_memory[col] += memory_feed[col] + ' '
#     for line in led_memory:
#         print(line)
#
#
# ok = False
# while not ok:
#     try:
#         user_input = input('Type in a non-negative integer number: ')
#         ok = user_input.isdigit() and len(user_input) > 0
#         if not ok:
#             print('It has to be integer! No floats, letters or special signs are allowed.')
#             continue
#     except ValueError:
#         print('Try integer not a float.')
#         continue
#     led_display(user_input)


patterns = [
    ['###', '# #', '# #', '# #', '###'],    # 0
    ['  #', '  #', '  #', '  #', '  #'],    # 1
    ['###', '  #', '###', '#  ', '###'],    # 2
    ['###', '  #', '###', '  #', '###'],    # 3
    ['# #', '# #', '###', '  #', '  #'],    # 4
    ['###', '#  ', '###', '  #', '###'],    # 5
    ['###', '#  ', '###', '# #', '###'],    # 6
    ['###', '  #', '  #', '  #', '  #'],    # 7
    ['###', '# #', '###', '# #', '###'],    # 8
    ['###', '# #', '###', '  #', '###']     # 9
    ]


def led_display(user_input):
    for row in range(len(patterns[0])):
        led_memory = []
        for digit in user_input:
            led_memory.append(patterns[int(digit)][row])
        print(' '.join(led_memory))


ok = False
while not ok:
    try:
        user_input = input('Type in a non-negative integer number: ')
        ok = user_input.isdigit() and len(user_input) > 0
        if not ok:
            print('It has to be integer! No floats, letters or special signs are allowed.')
            continue
    except ValueError:
        print('Try integer not a float.')
        continue
    led_display(user_input)
