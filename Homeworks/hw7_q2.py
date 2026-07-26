#Name: Aliasghar Rashidabadi
#Course: Advanced Programming
#Student ID: 40419533

class Animal(object):
    def __init__(self, age, name):
        self.petname = name
        self.years = age

    #getters
    def get_name(self):
        return self.petname
    def get_age(self):
        return self.years

def make_animal(l1, l2):
    l = []
    for j in range(len(l1)):
        #type of age and name are already checked in the main scope
        if l1[j] >= 0:
            l.append(Animal(l1[j], l2[j]))
    return l

#Main Scope
names = []
ages = []
amount = int(input("Enter how many you want to enter: "))

for i in range(amount):
    name = input(f"Enter name {i+1}: ")
    names.append(name)
    try:
        age = int(input(f"Enter age {i+1}: "))
        ages.append(age)
    except:
        raise ValueError("Entered Age must be an integer.")
answer = make_animal(ages, names)
for i in answer:
    print(f"Name: {i.get_name()}, Age: {i.get_age()}")