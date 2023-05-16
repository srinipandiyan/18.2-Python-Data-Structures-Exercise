def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    freq_table = {}
    for num in nums:
        if num not in freq_table:
            freq_table[num] = 1
        else:
            freq_table[num] += 1
    
    mode = None
    max_count = 0
    for num, count in freq_table.items():
        if count > max_count:
            mode = num
            max_count = count

    return mode
    

