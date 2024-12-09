"""
File Operations
---
"""
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class File_Operations:

    def __init__(self, filename:str):
        self.__filename = filename
        print(self.__filename)

    def read_file_content(self):
        try:
            with open(self.__filename, 'r') as f:
                self.__file_content = f.read()
                print(self.__file_content)
        except Exception as e:
            raise Exception(f"ERROR : File does not exist {self.__filename}{e}")

    def append_to_file(self, content:str):
        try:
            with open(self.__filename, 'a') as f:
                f.write(content)
        except Exception as e:
            raise Exception(f"ERROR : File does not exist {self.__filename}{e}")

    def delete_file(self, filename):
        try:
            relative_filename = os.path.join(ROOT_DIR, filename)
            option = input(f"Are you sure you want to delete file ({relative_filename})? (Y/N)").lower()
            if option == 'y':
                if os.path.exists(relative_filename):
                    os.remove(relative_filename)
                else:
                    raise Exception(f"ERROR : File does not exist {self.__filename}{e}")
        except Exception as e:
            raise Exception(f"ERROR : File does not exist {self.__filename}{e}")

try:
    fo = File_Operations(os.path.join(ROOT_DIR, 'hello.txt'))
    fo.read_file_content()
    fo.append_to_file(" hello")
    fo.delete_file('hello.txt')
except Exception as e:
    print(e)
