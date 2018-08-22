"""Initial solution to deep_add exercise

08/21/2018
"""


def deep_add(nested_list, start=0):
    q = [nested_list]
    while q:
        element = q.pop()
        try:
            # If the element is iterable, add its children to queue
            for child in element:
                q.append(child)
        except TypeError:
            # It's not iterable -- add it to the sum
            start += element
    return start
