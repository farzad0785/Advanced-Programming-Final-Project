import re

def is_capitalized(text):
    """Validation. return True if text is capitalized."""
    return bool(text and re.match(r'^[A-Z][a-z]*$', text))

def is_digits(text, amount):
    """Validation. return True if text has only and exactly 'amount' digits."""
    return bool(text and re.match(rf'^\d{{{amount}}}$', text))

#Not finished yet
"""Sorter algorithm based on merge sort. Sorts according to the user's choice. """
def merge_sort():
    pass
def merge():
    pass