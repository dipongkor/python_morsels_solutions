"""Initial solution to deep_add exercise

08/21/2018
"""


def deep_add(nested_list, start=0):
    stack = [nested_list]
    while stack:
        element = stack.pop()
        try:
            # If the element is iterable, add its children to queue
            for child in element:
                stack.append(child)
        except TypeError:
            # It's not iterable -- add it to the sum
            start += element
    return start
