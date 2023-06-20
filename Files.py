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
# import os
#
#
# data = bytearray(10)
#
# for i in range(len(data)):
#     data[i] = 10 + i
#
# try:
#     bf = open("file.bin", "wb")
#     bf.write(data)
#     bf.close()
# except IOError as e:
#     print("I/O error occurred:", os.strerror(e.errno))


# %%

# data = bytearray(10)
#
# for i in range(len(data)):
#     data[i] = 10 - i
#
# for b in data:
#     print(hex(b))


# %% 4.3.6 How to read bytes from a stream --> readinto()
# import os
#
# data = bytearray(10)
#
# try:
#     binary_file = open("file.bin", "rb")
#     binary_file.readinto(data)
#     binary_file.close()
#
#     for b in data:
#         print(hex(b), end=" ")
# except IOError as e:
#     print("I/O error occurred:", os.strerror(e.errno))


# %% # %% 4.3.6 How to read bytes from a stream --> read()
# import os
#
# try:
#     binary_file = open("file.bin", "rb")
#     data = bytearray(binary_file.read())
#     binary_file.close()
#
#     for b in data:
#         print(hex(b), end=" ")
#
# except IOError as e:
#     print("I/O error occurred:", os.strerror(e.errno))


# %%
# import os
#
# try:
#     binary_file = open("file.bin", "rb")
#     data = bytearray(binary_file.read(5))
#     binary_file.close()
#
#     for b in data:
#         print(hex(b), end=" ")
#
# except IOError as e:
#     print("I/O error occurred:", os.strerror(e.errno))


# %% 4.3.7 Copying files - a simple and functional tool
# import os
#
#
# srcname = input("Enter the source file name: ")
# try:
#     src = open(srcname, "rb")
# except IOError as e:
#     print("Cannot open the source file: ", os.strerror(e.errno))
#     exit(e.errno)
#
# dstname = input("Enter yhe destination file name: ")
# try:
#     dst = open(dstname, "wb")
# except IOError as e:
#     print("Cannot create the destination file: ", os.strerror(e.errno))
#     src.close()
#     exit(e.errno)
#
# buffer = bytearray(65536)
# total = 0
# try:
#     readin = src.readinto(buffer)
#     while readin > 0:
#         written = dst.write(buffer[:readin])
#         total += written
#         readin = src.readinto(buffer)
# except IOError as e:
#     print("Cannot create the destination file: ", os.strerror(e.errno))
#     exit(e.errno)
#
# print(total, "byte(s) successfully written")
# src.close()
# dst.close()


# %% 4.3.8 LAB -> Character frequency histogram - with sort by keys
import os


# def prompt():
#     source_name = input("Enter file name to be analysed: ")
#     try:
#         file = open(source_name, "rt")
#         return file
#     except IOError as e:
#         print("Cannot open source file.", os.strerror(e.errno))
#         exit(e.errno)
#
#
# def print_histogram(histogram):
#     # sorted_dict = dict(sorted(histogram.items()))
#     for key, value in histogram.items():
#         if value != 0:
#             print(key, "->", value)
#
#
# histogram = {chr(ch): 0 for ch in range(ord("a"), ord("z") + 1)}
# # histogram = {str(ch): 0 for ch in range(10)}
# file = prompt()
#
#
# for line in file:
#     for char in line:
#         if char.isdigit():
#             histogram[char.lower()] += 1
#         else:
#             continue
# file.close()
# print_histogram(histogram)


# %% 4.3.8 LAB -> Character frequency histogram - with sort by keys
# import os
#
#
# def prompt():
#     global source_name
#     source_name = input("Enter file name to be analysed: ")
#     try:
#         file = open(source_name, "rt")
#         return file
#     except IOError as e:
#         print("Cannot open source file.", os.strerror(e.errno))
#         exit(e.errno)
#
#
# def print_histogram(histogram):
#     histogram_s = dict(sorted(histogram.items(), key=lambda item: item[1], reverse=True))
#     for key, value in histogram_s.items():
#         if value != 0:
#             print(key, "->", value)
#
#
# def write_results(histogram, source_name):
#     histogram_s = dict(sorted(histogram.items(), key=lambda item: item[1], reverse=True))
#     try:
#         new_file = open(f"{source_name}.hist", "wt")
#         for key, value in histogram_s.items():
#             line = f"{key} -> {value}\n"
#             new_file.write(line)
#         new_file.close()
#     except IOError as e:
#         print("Cannot open source file.", os.strerror(e.errno))
#         exit(e.errno)
#
#
# histogram = {chr(ch): 0 for ch in range(ord("a"), ord("z") + 1)}
# # histogram = {str(ch): 0 for ch in range(10)}
# file = prompt()
#
#
# for line in file:
#     for char in line:
#         if char.isalpha():
#             histogram[char.lower()] += 1
#         else:
#             continue
#
# print_histogram(histogram)
# write_results(histogram, source_name)
# file.close()

# %% 4.3.10 LAB Evaluating students' results
import os


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line_no, source_name):
        super().__init__()
        self.line_no = line_no
        self.source_name = source_name


class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__()


def add_to_dict(dict_, data, student="", score=""):
    for char in data:
        if not char.isdigit() and char != ".":
            student += char
        elif char.isdigit() or char == ".":
            score += char
    if student.strip() in dict_:
        students_dict[student.strip()] += (score,)
    else:
        students_dict[student.strip()] = (score,)


def print_results(to_sort):
    to_print = dict(sorted(to_sort.items(), key=lambda item: item[1]))
    for key, item in to_print.items():
        total = 0
        for number in item:
            total += float(number)
        print(key, total)


source_name = input("Enter file name to process: ")
try:
    file = open(source_name, "rt")
    students_dict = {}

    a = file.readlines()
    if len(a) == 0:
        raise FileEmpty()

    line_no = 0

    file = open(source_name, "rt")
    for line in file:
        line_no += 1
        if len(line.split()) != 3:
            raise BadLine(line_no, source_name)
        test = float(line.split()[-1])
        add_to_dict(students_dict, line)
    file.close()
    print_results(students_dict)

except IOError as e:
    print("Error occurred", os.strerror(e.errno))
    exit(e.errno)
except BadLine as e:
    print(f"Bad data at line number {e.line_no} at sourcefile: {e.source_name}")
except FileEmpty:
    print("File is empty, nothing to process.")


# %%
