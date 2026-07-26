#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

class Coordinate(object):
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval

class Circle(object):
    def __init__(self, center, radius):
        if not isinstance(center, Coordinate):
            raise ValueError("Center must be a Coordinate class. ")
        try:
            self.radius = int(radius)
        except ValueError:
            raise ValueError("Radius must be an integer. ")

        self.center = center

x_val = int(input("Enter the x parameter of the center of the circle: "))
y_val = int(input("Enter the y parameter of the center of the circle: "))

while True:
    choice = int(input("Set the center: \n1- Manually. \n2- With coordinate class. \n: "))

    if choice == 1:
        o = (x_val, y_val)
        break
    elif choice == 2:
        o = Coordinate(x_val, y_val)
        break
    else:
        print("Invalid Input. Enter 1 or 2.")

r = input("Enter radius of the circle: ")
c = Circle(o, r)
print(f"Coordinate of the center of the circle: ({c.center.x}, {c.center.y}) "
      f"\nRadius of the circle: {c.radius}")