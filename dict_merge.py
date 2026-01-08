def merge_dicts(dict_primary, dict_secondary):
    # Start with a copy of the primary so we don't change the original
    result = dict_primary.copy()
    
    for key, value in dict_secondary.items():
        if key in result:
            # Conflict found: Check if it's already a list to avoid nesting
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            # No conflict: Just add the new key-value
            result[key] = value
            
    return result

# Small d1, Large d2
d1 = {'a': 1}
d2 = {'a': 2, 'b': 4, 'c': 6, 'd': 8}

final = merge_dicts(d1, d2)
print(final)
