class ParsedTag(object):
    def __init__(self, tag_string):
        if tag_string[0] != '<' or tag_string[-1] != '>':
            raise ValueError('Tag must begin with "<" and end with ">"')

        tag_string = tag_string[1:-1].lower()  # Strip < and >
        try:
            # Split off first chunk -- that's the tag name
            self.name, attribute_strs = tag_string.split(maxsplit=1)
        except ValueError:
            # Not enough values to unpack -- there are no attributes
            self.name, attribute_strs = tag_string, ""

        self.attributes = {}
        for attribute in attribute_strs.split():
            self.add_attribute(attribute)

    def __eq__(self, other):
        return self.name == other.name and self.attributes == other.attributes

    def add_attribute(self, attribute_str):
        if '=' in attribute_str:
            key, value = attribute_str.split('=')
        else:
            key, value = attribute_str, None
        if key not in self.attributes:
            # Don't update the key after we've seen it once
            self.attributes[key] = value


def tags_equal(tag1, tag2):
    return ParsedTag(tag1) == ParsedTag(tag2)
