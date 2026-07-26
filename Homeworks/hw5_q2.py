#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

def pairwise_div(lnum, ldenom):
    assert lnum or ldenom, "lnum (L1) or ldenom (L2) cannot be empty. "
    assert len(lnum) == len(ldenom), "lnum (L1) and ldenom (L2) must be equal length. "

    division_list = []
    for i in range(len(lnum)):
        try:
            lnum[i] = int(lnum[i])
            ldenom[i] = int(ldenom[i])
            if ldenom[i] == 0:
                raise ZeroDivisionError("in ldenom (L2) cannot be zero. ") #We can also use ValueError exception.
            division_list.append(lnum[i] / ldenom[i])
        except ValueError:
            raise ValueError("Cannot convert", lnum[i], "or", ldenom[i])

    return division_list

L1 = input("Enter L1 elements: ").split()
L2 = input("Enter L2 elements: ").split()
print(pairwise_div(L1, L2))