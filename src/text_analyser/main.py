'''
Module for Text Analyser
--
'''
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class File_Analyser:
    """
    A class for analyzing text files. Provides functionalities to read a file, 
    analyze its content, and extract useful information like word count, 
    character count, and word frequency.

    Attributes:
        __filename (str): The name of the file being analyzed.
        __file_content (str): The content of the file as a string.
        __paragraph (list[str]): Paragraphs of the file content split by newlines (internal use).
        __words (list[str]): List of words in the file content (internal use).
        __word_frequency (dict): Frequency of each word in the file content (internal use).
        __frequent_word (str): The most frequent word in the file content (internal use).
        __max_frequency (int): The frequency of the most frequent word (internal use).
    """
    def __init__(self, filename:str):
        """
        Initializes the File_Analyser with the provided filename and reads its content.

        Args:
            filename (str): The name of the file to analyze.

        Raises:
            Exception: If the file does not exist or cannot be opened.
        """
        self.__filename = filename
        try:
            with open(self.__filename, 'r') as f:
                self.__file_content = f.read()
        except Exception as e:
            raise Exception(f"ERROR : File does not exist {self.__filename}{e}")
    
    def get_file_content(self) -> str:
        """
        Retrieves the content of the file.

        Returns:
            str: The entire content of the file as a string.
        """
        return self.__file_content

    def get_words(self) -> list[str]:
        """
        Extracts and returns a list of words from the file content.

        Returns:
            list[str]: A list of words in lowercase and stripped of punctuation.
        """
        self.__paragraph = self.get_file_content().split('\n')
        self.__words = list()
        for p in self.__paragraph:    
            self.__words.extend(w for w in p.split(' '))
        self.__words = [w.strip(',?.;!:').lower() for w in self.__words]
        return self.__words

    def get_word_count(self) -> int:
        """
        Counts the number of words in the file content.

        Returns:
            int: The total number of words.
        """
        return len(self.get_words())

    def get_character_count(self) -> int:
        """
        Counts the number of characters in the file content.

        Returns:
            int: The total number of characters.
        """
        return len(self.get_file_content())
    
    def get_character_count_without_space(self) -> int:
        """
        Counts the number of characters in the file content without space.

        Returns:
            int: The total number of non-space characters.
        """
        return len(self.get_file_content().replace(' ', ''))
    
    def get_word_frequency(self) -> dict:
        """
        Calculates the frequency of each word in the file content.

        Returns:
            dict: A dictionary where keys are words and values are their frequencies.
        """
        self.__word_frequency = dict()
        for w in self.get_words():
            if w in self.__word_frequency.keys():
                self.__word_frequency[w] += 1
            else:
                self.__word_frequency[w] = 1
        return self.__word_frequency
    
    def get_most_frequent_word(self) -> tuple:
        """
        Finds the most frequent word in the file content.

        Returns:
            tuple: A tuple containing the most frequent word and its frequency.
        """
        self.get_word_frequency()
        self.__frequent_word = ''
        self.__max_frequency = 0
        for key, value in self.__word_frequency.items():
            if value >= self.__max_frequency:
                self.__max_frequency = value
                self.__frequent_word = key
        return self.__frequent_word, self.__max_frequency


def file_menu() -> int:
    print("-------------------------------------------")
    print("Welcome to File Analyser")
    print("Select from options below:")
    print("-------------------------------------------")
    print("1. Word Count")
    print("2. Character Count")
    print("3. Character Count (Without Space)")
    print("4. Most frequenct word")
    print("-------------------------------------------")
    print("Press any key to exit")
    print("-------------------------------------------")
    try: 
        return int(input("Enter option : "))
    except Exception as e:
        return 0

def start():
    try:
        fa = File_Analyser(os.path.join(ROOT_DIR, 'sample_file.txt'))
        option = 1
        while(option):
            option = file_menu()
            if (option == 1):
                print(f"\nWord count : {fa.get_word_count()}\n")
            elif(option == 2):    
                print(f"\nCharacter count : {fa.get_character_count()}\n") 
            elif(option == 3):
                print(f"\nCharacter count (Without Space) : {fa.get_character_count_without_space()}\n")  
            elif(option == 4):
                wf = fa.get_most_frequent_word()
                print(f"\nMost Frequent Word : {wf[0]} with frequency of {wf[1]}\n")
            else:
                print("\nExiting...")
    except Exception as e:
        print(e)

start()