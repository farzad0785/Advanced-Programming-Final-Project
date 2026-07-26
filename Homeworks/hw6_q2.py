#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

def deep_sum(data):
    if not data:
        return 0
    if isinstance(data[0], list):
        return deep_sum(data[0]) + deep_sum(data[1:])
    else:
        return data[0] + deep_sum(data[1:])

print(deep_sum([[[1]], 2, [[3, [4]]]]))