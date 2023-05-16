def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    truthy = []
    falsey = [0, '', [], False, (), None]
    for item in lst:
        if item not in falsey:
            truthy.append(item)
            
    return truthy
