"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List



def split_symbols(a):
    b = list(a)
    return b





def first_symbol_unicode_check(a):
    if '\\' in a[0]:
        return a[0:6], a[7:]
    else:
        return a[0], a[1:]




# def get_longest_diverse_words(file_path: str) -> List[str]:
#     words_unique = {}
#     symbol_unique = {}
#     with open('data.txt', 'r') as data:
#         for line in data:
#             line = line.rstrip()
#             line = line.split(' ')
#             print('line', line)
#             for word in line:
#                 if word is not '':
#                     symbol_unique[word] = 0
#                     print('word', word)
#
#                     word_1 = word;
#                     while word_1:
#                         symbol = first_symbol_unicode_check(word_1)
#                         print('symbol_check', symbol)
#                         # word_1 = word_1[1:]
#                         word_1 = symbol[1]
#                         if symbol[0] not in symbol_unique:
#                             symbol_unique[word] += 1
#                         else:
#                             symbol_unique[word] = 1
#
#             return symbol_unique
#         # return symbol_unique



# print(get_longest_diverse_words('data.txt'))









def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...
