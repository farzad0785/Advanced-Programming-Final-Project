#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming


def compress_string_recur(s: str) -> str:
    #Base cases:
    if len(s) == 1:
        return s[0] + "1"

    #Counting consecutive characters
    counter = 0
    for i in range(len(s)):
        if s[i] != s[0]:
            break
        counter += 1

    #Prevent counting spaces
    if s[0] == " ":
        return "" + compress_string_recur(s[counter: ])

    #Recrusive step
    return s[0] + str(counter) + compress_string_recur(s[counter: ])

user_str = input("Enter your string: ")
print(compress_string_recur(user_str))