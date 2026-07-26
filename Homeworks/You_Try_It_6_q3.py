#Name: Aliasghar Rashidabadi
#Student ID: 4419533
#Course: Advanced Programming

def in_list_of_lists(l, e):
    if len(l) == 0:
        return False
    elif e in l[0]:
        return True

    return in_list_of_lists(l[1: ], e)
user_list = input("Enter your list of numbers list: (e.g. 1 2 3;4 5;6 7) : ").split(";")

#Turning the list of numbers to a list containing lists of numbers.
for i in range(len(user_list)):
    user_list[i] = user_list[i].split()

user_e = input("Enter the element to look for in the list of lists: ")
print(in_list_of_lists(user_list, user_e))