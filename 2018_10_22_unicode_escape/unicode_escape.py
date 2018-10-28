import sys


def unicode_escape(filepath):
    with open(filepath, mode='rt', encoding='utf-8') as file:
        escaped_string = ""
        for c in file.read():
            if ord(c) > 127:
                try:
                    escaped_string += r"\U{0:0>8}".format(hex(ord(c))[2:])
                except IndexError:
                    raise IndexError("Value of type(c): {}".format(type(ord(c))))
            else:
                escaped_string += c
        print(escaped_string, end='')


if __name__ == '__main__':
    unicode_escape(sys.argv[1])
