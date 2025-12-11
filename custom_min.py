def return_min(*args):
    # If no arguments are provided, raise a ValueError
    if not args:
        raise ValueError("return_min() requires at least one argument")
    
    # Initialize min_value with the first argument
    min_value = args[0]
    
    # Loop through the remaining arguments
    for arg in args[1:]:
        # Update min_value if a smaller value is found
        if min_value > arg:
            min_value = arg
    
    # Return the smallest value
    return min_value


t = return_min(7,-1,6,4,9)
print(t)
