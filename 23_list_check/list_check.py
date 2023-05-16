def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    counter = 0
    for item in lst:
        if isinstance(item, list):
            counter += 1
    
    if counter == len(lst):
        return True
    
    return False