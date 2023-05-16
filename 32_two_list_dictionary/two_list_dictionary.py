def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    my_dict = {}
    if len(keys) == len(values) or len(keys) < len(values):
        for i in range(len(keys)):
            my_dict[keys[i]] = values[i]
    elif len(keys) > len(values):
        max_value_i = len(values)
        for i in range(len(keys)):
            if i < max_value_i:
                my_dict[keys[i]] = values[i]
            else:
                my_dict[keys[i]] = None
    return my_dict