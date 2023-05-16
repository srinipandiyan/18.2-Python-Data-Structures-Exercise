def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    string = ""
    for char in phrase:
        if to_swap == char:
            string += char.swapcase()
        elif to_swap.swapcase() == char:
            string += char.swapcase()
        else:
            string += char
    return string