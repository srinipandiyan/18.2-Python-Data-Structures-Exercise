def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    my_list = list(phrase)
    my_string = ''.join(my_list[::-1])
    return my_string
