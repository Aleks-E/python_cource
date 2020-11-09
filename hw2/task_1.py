"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List

import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    words_unique = {}
    with open("file_path", "r") as data:
        for line in data:
            line = line.rstrip()
            line = line.split(' ')
            for word in line:
                if word != '':
                    word = word.encode().decode('unicode-escape')
                    word = word.translate(word.maketrans("", "", string.punctuation))
                    word = word.replace('»', '')
                    word = word.replace('«', '')
                    if word not in words_unique:
                        words_unique[word] = len(set(word))

        words_list = list(words_unique.items())
        words_list.sort(key=lambda x: x[1], reverse=True)
        longest_unique_words = []
        for i in range(10):
            longest_unique_words.append(words_list[i][0])

        return longest_unique_words





# def get_rarest_char(file_path: str) -> str:
#     chars = {}
#     with open('data.txt', 'r') as data:
#         for line in data:
#             line = line.rstrip()







def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...




# print(get_longest_diverse_words('data.txt'))

