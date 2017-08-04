"""
    collection of operations that deal with nones/ not exists
"""


def ifnone(none_var, replace_var=''):
    """Simple handler for None values."""
    if none_var:
        return none_var
    return replace_var


def ifnokey(dct, key, rep_var=None):
    """If the key of the dict is not found, it returns the rep_var's value."""
    try:
        return dct[key]
    except KeyError:
        return rep_var

