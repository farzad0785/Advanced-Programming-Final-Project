#Name: Aliasghar Rashidabadi
#Student ID: 4419533
#Course: Advanced Programming

def power_recur(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    return n * power_recur(n, p-1)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent(Must not be negative) : "))
while exponent < 0:
    exponent = int(input("Exponent cannot be negative. \nTry again: "))
    if exponent >= 0:
        break

print(power_recur(base, exponent))