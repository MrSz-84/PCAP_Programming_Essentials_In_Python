# %% 4.2.5 Opening the streams

# stream = open(file, mode='r', encoding=None)

# opening modes
"""
r open mode: read

    the stream will be opened in read mode;
    the file associated with the stream must exist and has to be readable, otherwise the open() function raises an exception.

w open mode: write

    the stream will be opened in write mode;
    the file associated with the stream doesn't need to exist; if it doesn't exist it will be created; if it exists, it will be truncated to the length of zero (erased); if the creation isn't possible (e.g., due to system permissions) the open() function raises an exception.

a open mode: append

    the stream will be opened in append mode;
    the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; if it exists the virtual recording head will be set at the end of the file (the previous content of the file remains untouched).

r+ open mode: read and update

    the stream will be opened in read and update mode;
    the file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception;
    both read and write operations are allowed for the stream.

w+ open mode: write and update

    the stream will be opened in write and update mode;
    the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; the previous content of the file remains untouched;
    both read and write operations are allowed for the stream.
"""

# %% 4.2.8 Pre-opened streams

"""
We said earlier that any stream operation must be preceded by the open() function invocation. There are three well-defined exceptions to the rule.

When our program starts, the three streams are already opened and don't require any extra preparations. What's more, your program can use these streams explicitly if you take care to import the sys module:

import sys
 


because that's where the declaration of the three streams is placed.

The names of these streams are: sys.stdin, sys.stdout, and sys.stderr.

Let's analyze them:

    sys.stdin
        stdin (as standard input)
        the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs;
        the well-known input() function reads data from stdin by default.

    sys.stdout
        stdout (as standard output)
        the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program;
        the well-known print() function outputs the data to the stdout stream.

    sys.stderr
        stderr (as standard error output)
        the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where the running program should send information on the errors encountered during its work;
        we haven't presented any method to send the data to this stream (we will do it soon, we promise)
        the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably useful but does not provide results) gives the possibility of redirecting these two types of information to the different targets. More extensive discussion of this issue is beyond the scope of our course. The operation system handbook will provide more information on these issues.
"""


# %% 4.2.10 Diagnosing stream problems

"""

The IOError object is equipped with a property named errno (the name comes from the phrase error number) and you can access it as follows:

try:
    # Some stream operations.
except IOError as exc:
    print(exc.errno)
 


The value of the errno attribute can be compared with one of the predefined symbolic constants defined in the errno module.

Let's take a look at some selected constants useful for detecting stream errors:

    errno.EACCES → Permission denied

    The error occurs when you try, for example, to open a file with the read only attribute for writing.

    errno.EBADF → Bad file number

    The error occurs when you try, for example, to operate with an unopened stream.

    errno.EEXIST → File exists

    The error occurs when you try, for example, to rename a file with its previous name.

    errno.EFBIG → File too large

    The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.

    errno.EISDIR → Is a directory

    The error occurs when you try to treat a directory name as the name of an ordinary file.

    errno.EMFILE → Too many open files

    The error occurs when you try to simultaneously open more streams than acceptable for your operating system.

    errno.ENOENT → No such file or directory

    The error occurs when you try to access a non-existent file/directory.

    errno.ENOSPC → No space left on device

    The error occurs when there is no free space on the media.

The complete list is much longer (it also includes some error codes not related to the stream processing).

"""

# %% 4.3.1 Processing text files


# import errno
#
# try:
#     s = open("c:/users/user/Desktop/file.txt", "rt")
#     s.close()
# except Exception as exc:
#     if exc.errno == errno.ENOENT:
#         print("The file doesn't exist.")
#     elif exc.errno == errno.EMFILE:
#         print("You've opened too many files.")
#     else:
#         print("The error number is:", exc.errno)
#
#
# from os import strerror
#
# try:
#     s = open("c:/users/user/Desktop/file.txt", "rt")
#     s.close()
# except Exception as exc:
#     print("The file could not be opened:", strerror(exc.errno))


# %%
# import os
#
# try:
#     counter = 0
#     stream = open("text.txt", "rt")
#     char = stream.read(1)
#     while char != "":
#         print(char, end="")
#         counter += 1
#         char = stream.read(1)
#     stream.close()
#     print("\n\nCharacters in file:", counter)
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))


# %%
# import os
#
# try:
#     counter = 0
#     stream = open("text.txt", "rt")
#     content = stream.read()
#     for char in content:
#         print(char, end="")
#         counter += 1
#     stream.close()
#     print("\n\nCharacters in file:", counter)
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))


# %%
# import os
#
# try:
#     counter = 0
#     stream = open("C:\\Users\\pixel\\Downloads\\sudoku.csv\\sudoku.csv", "rt")
#     char = stream.read(1)
#     while char != "":
#         print(char, end="")
#         counter += 1
#         char = stream.read(1)
#     stream.close()
#     print("\n\nCharacters in file:", counter)
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))


# %%
# import os
#
# try:
#     counter = 0
#     stream = open("C:\\Users\\pixel\\Downloads\\sudoku.csv\\sudoku.csv", "rt")
#     content = stream.read()
#     for char in content:
#         counter += 1
#     stream.close()
#     print("\n\nCharacters in file:", counter)
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))

# %% 4.3.2 readline()
# import os
#
# try:
#     character_counter = line_counter = 0
#     stream = open("text.txt", "rt")
#     line = stream.readline()
#     while line != "":
#         line_counter += 1
#         for char in line:
#             print(char, end="")
#             character_counter += 1
#         line = stream.readline()
#     stream.close()
#     print("\n\nCharacters in file:", character_counter)
#     print("Lines in file:", line_counter)
# except IOError as e:
#     print("I/O error occurred:", os.strerror(e.errno))

# %%
# import os
#
# try:
#     character_counter = line_counter = 0
#     stream = open("C:\\Users\\pixel\\Downloads\\sudoku.csv\\sudoku.csv", "rt")
#     line = stream.readline()
#     while line != "":
#         line_counter += 1
#         for char in line:
#             character_counter += 1
#         line = stream.readline()
#     stream.close()
#     print("\n\nCharacters in file:", character_counter)
#     print("Lines in file:", line_counter)
# except IOError as e:
#     print("I/O error occurred:", os.strerror(e.errno))


# %% 3.3.3 readlines()
# stream = open("text.txt")
# print(stream.readlines(20))
# print(stream.readlines(20))
# print(stream.readlines(20))
# print(stream.readlines(20))
# stream.close()

# %%
# stream = open("C:\\Users\\pixel\\Downloads\\sudoku.csv\\sudoku.csv")
# print(stream.readlines(20))
# print(stream.readlines(20))
# print(stream.readlines(20))
# print(stream.readlines(20))
# stream.close()

# %%
# import os
#
# try:
#     ccnt = lcnt = 0
#     s = open("text.txt", "rt")
#     lines = s.readlines(20)
#     while len(lines) != 0:
#         for line in lines:
#             lcnt += 1
#             for ch in line:
#                 print(ch, end="")
#                 ccnt += 1
#         lines = s.readlines(10)
#     s.close()
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred:", os.strerror(e.errno))

# %%

# import os
#
# try:
#     ccnt = lcnt = 0
#     s = open("C:\\Users\\pixel\\Downloads\\sudoku.csv\\sudoku.csv", "rt")
#     lines = s.readlines(20)
#     while len(lines) != 0:
#         for line in lines:
#             lcnt += 1
#             for ch in line:
#                 ccnt += 1
#         lines = s.readlines(10)
#     s.close()
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred:", os.strerror(e.errno))

# %%
#
# import os
#
# try:
#     ccnt = lcnt = 0
#     for line in open("text.txt", "rt"):
#         lcnt += 1
#         for ch in line:
#             print(ch, end="")
#             ccnt += 1
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))

# %% 4.3.4 Dealing with text files: write()

# import os
#
# try:
#     file = open("newtext.txt", "wt")  # a new file is created.
#     for i in range(10):
#         s = "line #" + str(i + 1) + "\n"
#         for char in s:
#             file.write(char)
#     file.close()
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))
#
# # %% printing created files contents.
# try:
#     file = open("newtext.txt", "rt")
#     line = file.readline()
#     while line != "":
#         for char in line:
#             print(char, end="")
#         line = file.readline()
#     file.close()
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))


# %% writing whole lines

# import os
#
# try:
#     file = open("newtext.txt", "wt")
#     for i in range(10):
#         file.write("line #$#" + str(i + 1) + "\n")
#     file.close()
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))
#
#
# try:
#     file = open("newtext.txt", "rt")
#     for line in file:
#         print(line, end="")
#     file.close()
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))

# %% writing whole lines
# import os
#
#
# try:
#     line_cnt = 0
#     source = open("C:\\Users\\pixel\\Downloads\\sudoku.csv\\demo_list.csv", "rt")
#     destination = open("C:\\Users\\pixel\\Downloads\\sudoku.csv\\demo_list.txt", "wt")
#     for line in source:
#         line_cnt += 1
#         make_copy = line
#         destination.write(line)
#     print("Lines copied: ", line_cnt)
# except IOError as e:
#     print("I/O error occurred: ", os.strerror(e.errno))


# %% 4.3.5 What is a bytearray
import os


data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open("file.bin", "wb")
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", os.strerror(e.errno))


# %%

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

