#!/usr/bin/env python

import sys


def escape(char):
    if ord(char) > 127:
        return r"\U{0:0>8}".format(hex(ord(char))[2:])
    else:
        return char


def escape_file(file):
    return "".join([
        escape(c)
        for c in file.read()
    ])


if __name__ == '__main__':
    filepath = sys.argv[1]
    if filepath == "-":
        # Read from stdin
        print(escape_file(sys.stdin), end='')
    else:
        with open(filepath, mode='rt', encoding='utf-8') as file:
            print(escape_file(file), end='')
