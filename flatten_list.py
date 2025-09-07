def flatten(nested_list):
    """Recursively flattens a list with irregular nesting."""
    for item in nested_list:
        if isinstance(item, list):
            # If the item is a list, yield from the result of flattening it
            yield from flatten(item)
        else:
            # If the item is not a list, yield the item itself
            yield item

# Example
my_list = [[['a', 'b', 'c'], [1, 2, 3], ['X', 'Y', 'Z'], [4, 5]], [6, 7, 9],[4,2,1]]

# The function returns a generator, so we convert it to a list
flat_list = list(flatten(my_list))

print(flat_list)
