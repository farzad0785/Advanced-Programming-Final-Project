#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

def deep_max_depth(data):
    if not isinstance(data, list):
        return 0
    if not data:
        return 1

    first = data[0]
    if isinstance(first, list):
        depth_first = 1 + deep_max_depth(first)
    else:
        depth_first = 1

    return max(depth_first, deep_max_depth(data[1:]))

#Edit this test case with whatever you want.
test = [1,[2,[3,[4]]]]

print(deep_max_depth(test))

