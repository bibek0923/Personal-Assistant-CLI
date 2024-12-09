'''
Module for Text Analyser
--
'''
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class File_Analyser:
    
    def __init__(self, filename:str):
        self.__filename = filename
        try:
            with open(self.__filename, 'r') as f:
                self.__file_content = f.read()
        except Exception as e:
            raise Exception(f"ERROR : File does not exist {self.__filename}{e}")
    
    def get_file_content(self) -> str:
        return self.__file_content

    def get_words(self) -> list[str]:
        self.__paragraph = self.get_file_content().split('\n')
        self.__words = list()
        for p in self.__paragraph:    
            self.__words.extend(w for w in p.split(' '))
        self.__words = [w.strip(',?.;!:').lower() for w in self.__words]
        return self.__words

    def get_word_count(self) -> int:
        return len(self.get_words())

    def get_character_count(self) -> int:
        return len(self.get_file_content())
    
    def get_word_frequency(self) -> dict:
        self.__word_frequency = dict()
        for w in self.get_words():
            if w in self.__word_frequency.keys():
                self.__word_frequency[w] += 1
            else:
                self.__word_frequency[w] = 1
        return self.__word_frequency
    
    def get_most_frequent_word(self) -> str:
        self.__frequent_word = ''
        frequency = 0
        for key, value in self.__word_frequency.items():
            if value >= frequency:
                frequency = value
                self.__frequent_word = key
        print(f"Most frequent word is {self.__frequent_word} with frequency of {frequency}")
        return self.__frequent_word

try:
    fa = File_Analyser(os.path.join(ROOT_DIR, 'sample_file.txt'))
    print(f"Word count : {fa.get_word_count()}") # 618 Words
    print(f"Character count : {fa.get_character_count()}")  
    print(f"Words Frequency : {fa.get_word_frequency()}")
    print(f"Most Frequent Word : {fa.get_most_frequent_word()}")
except Exception as e:
    print(e)