"""
File Operations
---
"""
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class File_Operations:
    """
    A class for performing file operations such as reading, appending content, 
    and deleting files. Handles errors gracefully when files are not found.

    Attributes:
        __filename (str): The name of the file on which operations will be performed.
        __file_content (str): The content of the file (retrieved during read operation).
    """

    def __init__(self, filename:str):
        """
        Initializes the File_Operations class with the provided filename.

        Args:
            filename (str): The name of the file to perform operations on.
        """
        self.__filename = filename

    def read_file_content(self):
        """
        Reads the content of the file and prints it to the console.

        Raises:
            Exception: If the file does not exist or cannot be opened.
        """
        try:
            with open(self.__filename, 'r') as f:
                self.__file_content = f.read()
                print(self.__file_content)
        except Exception as e:
            raise Exception(f"ERROR : File does not exist {self.__filename}{e}")

    def append_to_file(self, content:str):
        """
        Appends the specified content to the file.

        Args:
            content (str): The content to append to the file.

        Raises:
            Exception: If the file does not exist or cannot be opened.
        """
        try:
            with open(self.__filename, 'a') as f:
                f.write(content)
        except Exception as e:
            raise Exception(f"ERROR : File does not exist {self.__filename}{e}")

    def delete_file(self, filename):
        """
        Deletes the specified file after user confirmation.

        Args:
            filename (str): The name of the file to delete.

        Raises:
            Exception: If the file does not exist or cannot be deleted.
        """
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
