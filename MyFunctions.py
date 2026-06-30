import re

def is_capitalized(text):
    return bool(text and re.match(r'^[A-Z][a-z]*$', text))

def is_digits(text, amount):
    return bool(text and re.match(rf'^\d{{{amount}}}$', text))

#Not finished yet
def merge_sort():
    pass
def merge():
    pass