# %% 4.4.2 Getting information about the operating system
#
# import platform
# print(platform.uname())
#
# import os
# print(os.name)

# %% 4.4.3 Creating directories in Python mkdir()
# import os
#
# os.mkdir("my_first_directory")
# print(os.listdir())

# %% 4.4.4 Recursive directory creation makedirs()
# import os
#
# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.listdir())


# %% 4.4.5 Where am I now? getcwd()
# import os
#
# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.getcwd())
# os.chdir("my_second_directory")
# print(os.getcwd())

# %% 4.4.6 Deleting directories in Python rmdir()
# import os
#
# os.mkdir("my_first_directory")
# print(os.listdir())
# os.rmdir("my_first_directory")
# print(os.listdir())

# %% removedirs()
# import os
#
# os.makedirs("my_first_directory/my_second_directory")
# os.removedirs("my_first_directory/my_second_directory")
# print(os.listdir())


# %% 4.4.7 The system() function
# import os
#
# returned_value = os.system("mkdir my_first_directory")
# print(returned_value)
# print(os.listdir())

# %% 4.4.8 LAB The os module: LAB ---> my solution
import os


class Seeker:
    def __init__(self, path, dir_):
        self.path = path
        self.dir_ = dir_
        self.to_find = self.dir_

    def __str__(self, dirpath):
        print(f"...{dirpath[dirpath.find(self.path[2:])-1:]}")

    def find(self, directory="", to_find=""):
        if self.path[2:] in os.listdir():
            os.chdir(self.path)
        to_find = self.to_find
        directory = os.listdir()
        if os.getcwd().endswith(to_find):
            self.__str__(os.getcwd())
        for folder in directory:
            os.chdir(folder)
            self.find(folder, to_find)
            os.chdir("../")


def create_dir_structure():
    os.makedirs("./tree/c/other_courses/cpp")
    os.mkdir("./tree/c/other_courses/python")
    os.chdir("./tree")
    os.makedirs("cpp/other_courses/c")
    os.mkdir("./cpp/other_courses/python")
    os.makedirs("python/other_courses/c")
    os.mkdir("./python/other_courses/cpp")
    os.chdir("../")


create_dir_structure()
obj = Seeker(path="./tree", dir_="python")
obj.find()


# %% Sample solution
# import os
#
#
# class DirectorySearcher:
#     def find(self, path, dir):
#         try:
#             os.chdir(path)
#         except OSError:
#             # Doesn't process a file that isn't a directory.
#             return
#
#         current_dir = os.getcwd()
#         for entry in os.listdir("."):
#             if entry == dir:
#                 print(os.getcwd() + "/" + dir)
#             self.find(current_dir + "/" + entry, dir)
#
#
# directory_searchv3er = DirectorySearcher()
# directory_searchv3er.find("./tree", "python")

