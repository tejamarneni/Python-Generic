def combine_dicts_on_clash(d1, d2):
    # Start by making a copy of d1.
    # This correctly preserves all of d1's unique items.
    combined_dict = d1.copy()

    # Now, loop through the second dictionary
    for key, val2 in d2.items():
        
        if key not in combined_dict:
            # --- Case 1: New Key ---
            # The key is only in d2, so add it as-is.
            combined_dict[key] = val2
        else:
            # --- Case 2: Key Clash ---
            # The key is in both d1 and d2.
            val1 = combined_dict[key]
            
            # Start building the new list
            new_list = []

            # Add the first value (from d1)
            if isinstance(val1, list):
                new_list.extend(val1)
            else:
                new_list.append(val1)
            
            # Add the second value (from d2)
            if isinstance(val2, list):
                new_list.extend(val2)
            else:
                new_list.append(val2)
            
            # Update the dictionary with the new combined list
            combined_dict[key] = new_list
            
    return combined_dict

# --- Example ---
# 'a' clashes (item + list)
# 'b' clashes (list + item)
# 'c' is unique to d2 (item)
# 'y' is unique to d1 (list)

d1 = {'a': 1, 'b': [2, 3], 'y': [100, 200]}
d2 = {'a': [4, 5], 'b': 6, 'c': 7}

combined = combine_dicts_on_clash(d1, d2)
print(combined)