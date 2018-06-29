"""Second attempt, including bonus where
accented Latin characters are coerced to
basic ASCII characters

06/28/18
"""


import unicodedata
from collections import Counter


def is_anagram(string1, string2):
    def to_counter(string):
        """Normalize string and return a Counter object"""
        string = unicodedata.normalize('NFD', string)
        string = [
            char
            for char in string.lower()
            if char.isalpha()
        ]
        return Counter(string)
    return to_counter(string1) == to_counter(string2)
