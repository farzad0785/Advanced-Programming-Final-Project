#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

#before_debugging
def flatten_not_debugged(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        #This part needs to be debugged. It only returns the first element of the list. For example if the list has
        #3 elements, It only checks the first one, and doesn't return the rest.
        return flatten_not_debugged(lst[0])
    else:
        return [lst[0]] + flatten_not_debugged(lst[1:])

#After debugging
def flatten(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        #It is fixed now. It returns the rest of the elements to the function either.
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])

test = [1,2,[3,4,[5,6],7],8,[9],[10]]
print(flatten_not_debugged(test))
print(flatten(test))