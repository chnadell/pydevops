def flipper(string: str, reverse: bool=True, capitalize: bool=False):

    string_out = string
    if reverse:
        string_out = string[::-1]
    if capitalize:
        string_out = string_out.upper()

    return string_out
