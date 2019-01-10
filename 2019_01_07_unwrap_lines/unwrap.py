def unwrap_lines(wrapped_string):
    unwrapped_string = ""
    newlines = ""
    for char in wrapped_string:
        if char == "\n":
            newlines += char
        else:
            if len(newlines) > 1:
                unwrapped_string += newlines
            elif len(newlines) == 1:
                unwrapped_string += " "
            newlines = ""
            unwrapped_string += char
    return unwrapped_string
