"""Two initial solutions to the is_anagram exercise

06/25/2018
"""
from collections import Counter


def is_anagram(string1, string2):
    """Determine if two strings are anagrams.

    Spaces and non-alphanumeric characters are ignored
    """
    def to_sorted_list(string):
        return sorted([
            char
            for char in string.lower()
            if char.isalnum()
        ])
    return to_sorted_list(string1) == to_sorted_list(string2)


def is_anagram_alt(string1, string2):
    """Alternate implmentation"""
    def to_counter_dict(string):
        return dict(Counter([
            char
            for char in string.lower()
            if char.isalnum()
        ]))
    return to_counter_dict(string1) == to_counter_dict(string2)
