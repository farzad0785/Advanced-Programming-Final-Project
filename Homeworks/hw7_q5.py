#Name: Aliasghar Rashidabadi
#Course: Advanced Programming
#Student ID: 40419533

class Vehicle(object):
    def __init__(self, model, make):
        self.model = model
        #I suppose make attribute is the year of the manufacture
        self.make = make
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, new_make):
        if new_make < 1886 or new_make > 2026:
            raise ValueError("Invalid input. Make date (year of manufacture) must be between 1886 and 2026. ")
        self._make = new_make

    def info(self):
        return f"Vehicle: model: {self.model}, make: {self.make}"

class Car(Vehicle):
    def __init__(self, model, make, num_doors):
        super().__init__(model, make)
        self.num_doors = num_doors

    @property
    def num_doors(self):
        return self._num_doors

    @num_doors.setter
    def num_doors(self, new_doors):
        if new_doors != 2 and new_doors != 4:
            raise ValueError("Invalid input. doors amount must be 2 or 4.")
        self._num_doors = new_doors

    def info(self):
        return f"Car: Model: {self.model}, Make: {self.make}, Number of doors: {self.num_doors}"

#Main Scope
while True:
    try:
        #creating appropriate object according to the user choice (or even exiting).
        vehicle_type = int(input("Enter: \n\t1. Vehicle \n\t2. Car \n\t3. exit \n"))
        if vehicle_type not in (1,2,3):
            print("Invalid input. Entered integer must be 1 or 2 or 3. ")
            continue
    except ValueError:
        print("Invalid input. Enter an integer")
        continue

    #exit scope
    if vehicle_type == 3:
        print("exiting.")
        break

    model = input("Enter the model: ")
    try:
        make = int(input(f"Enter the make (year of manufacture): "))
    except ValueError:
        print("Invalid input. Enter numbers for make (year of manufacture). ")
        continue

    #vehicle object scope
    if vehicle_type == 1:
        #error handling for creating the vehicle object
        try:
            vehicle_obj = Vehicle(model, make)
        except ValueError as e:
            print(e)
            continue

        #info() method
        print(vehicle_obj.info())
        #skips the rest of the code which is for the Car subclass
        continue

    #car object scope
    try:
        num_doors = int(input("Enter the number of doors: "))
        car_obj = Car(model, make, num_doors)
    #error handling for setting the values when creating the object
    except ValueError as e:
        print(e)
        continue
    print(car_obj.info())