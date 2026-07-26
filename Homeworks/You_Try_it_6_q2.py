#Name: Aliasghar Rashidabadi
#Student ID: 4419533
#Course: Advanced Programming

def total_len_recur(l):
    if len(l) == 1:
        return len(l[0])
    return len(l[0]) + total_len_recur(l[1:])

test = input("Enter your desired string (WARNING: function does not count space as a character.) : ").split()
print(total_len_recur(test))