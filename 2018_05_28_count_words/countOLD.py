def count_words(text):
    filtered_string = ""
    word_counts = {}
    for index, char in enumerate(text):
        if char.isalnum() or char.isspace():
            # Alphanumeric and whitespace characters should be added
            # to filtered_string
            filtered_string += char
        else:
            # Non-alphanumeric characters should only be added if they
            # are surrounded on either side by alphanumeric chars (e.g.,
            # they are embedded within a word)
            try:
                if (text[index-1].isalnum() and
                        text[index+1].isalnum()):
                    filtered_string += char
            except IndexError:
                # Raised when char is first or last character in text
                pass
    filtered_string = filtered_string.lower()  # Make lowercase
    words = filtered_string.split()  # By default, splits on whitespace
    for word in words:
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 1
    return word_counts
