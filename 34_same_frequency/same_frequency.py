def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    freq_table_1 = {}
    for num in str(num1):
        if num not in freq_table_1:
            freq_table_1[num] = 1
        else:
            freq_table_1[num] += 1
    for num in str(num2):
        if num in freq_table_1:
            freq_table_1[num] -= 1
        else:
            freq_table_1[num] = 1
    return bool(all(value == 0 for value in freq_table_1.values()))