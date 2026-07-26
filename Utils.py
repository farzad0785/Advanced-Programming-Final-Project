import re

def is_capitalized(text):
    """Validation. return True if text is capitalized."""
    return bool(text and re.match(r'^[A-Z][a-z]*$', text))

def is_digits(text, amount):
    """Validation. return True if text has only and exactly 'amount' digits."""
    return bool(text and re.match(rf'^\d{{{amount}}}$', text))

def is_course_code_valid(text):
    """Validation. return True if text has 8 digits followed by exactly 3 letters. """
    return bool(text and re.match(r'^\d{8}[A-Za-z]{3}$', text))

def merge_sort(lst, key):
    if key.lower() not in ("gpa",  "total unit", "first name", "last name"):
        raise ValueError("Invalid input. Sorting is available for 'gpa', 'total unit', 'first/last name'. ")
    """Sorter algorithm based on merge sort. Sorts according to the user's choice. """
    if len(lst) < 2:
        return lst[:]
    middle = len(lst)//2
    left = merge_sort(lst[:middle], key)
    right = merge_sort(lst[middle:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i,j = 0,0
    if key.lower() == "gpa":
        while i < len(left) and j < len(right):
            if left[i][1].gpa >= right[j][1].gpa:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    elif key.lower() == "first name":
        while i < len(left) and j < len(right):
            if left[i][1].f_name >= right[j][1].f_name:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1

    elif key.lower() == "total unit":
        while i < len(left) and j < len(right):
            if left[i][1].total_unit >= right[j][1].total_unit:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    else:
        while i < len(left) and j < len(right):
            if left[i][1].l_name >= right[j][1].l_name:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result