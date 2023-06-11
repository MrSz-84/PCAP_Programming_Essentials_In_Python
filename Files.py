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

# %%


import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)


from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
