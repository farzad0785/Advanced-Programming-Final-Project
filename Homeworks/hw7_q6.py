#Name: Aliasghar Rashidabadi
#Course: Advanced Programming
#Student ID: 40419533

class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    #(protected) name getter
    @property
    def name(self):
        return self._name
    #(protected) name setter
    @name.setter
    def name(self, new_name):
        self._name = new_name

    #(protected) salary getter
    @property
    def salary(self):
        return self._salary
    #(protected) salary setter with validation
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid input. Salary cannot be negative. ")
        self._salary = new_salary

    def annual_bonus(self):
        return 0.05 * self._salary
    #summery of the Employee object
    def __str__(self):
        return (f"Worker: Employee \nName: {self.name} \nSalary: {self.salary} "
                f"\nAnnual bonus: {self.annual_bonus()}")

#Manager subclass
class Manager(Employee):
    #Manager class constructor
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    #team size getter
    @property
    def team_size(self):
        return self._team_size
    #team size setter
    @team_size.setter
    def team_size(self, members):
        if members < 0:
            raise ValueError("Invalid input. Team size cannot be negative. ")
        self._team_size = members

    def annual_bonus(self):
        return (0.1 * self.salary) + (500 * self.team_size)

    #summery of the manager object
    def __str__(self):
        return (f"Worker: Manager \nName: {self.name} \nSalary: {self.salary} \nTeam size: {self.team_size} "
                f"\nAnnual bonus: {self.annual_bonus()}")

#Main Scope

#program runs until user desire to exit
while True:
    try:
        #creating appropriate object according to the user choice (or even exiting).
        career = int(input("Enter: \n\t1. Employee \n\t2. Manager \n\t3. exit \n"))
        if career not in(1,2,3):
            print("Invalid input. Enter 1 or 2 or 3")
            continue
    except ValueError:
        print("Invalid input. Enter an integer. ")
        continue

    #exit scope
    if career == 3:
        print("exiting.")
        break

    name = input(f"Enter the name: ")
    try:
        salary = float(input("Enter the salary: "))
    except ValueError:
        print("Invalid input. Salary must be a number. ")
        continue

    if career == 1:
        #error handling for creating the employee object
        try:
            employee_obj = Employee(name, salary)
        except ValueError as e:
            print(e)
            continue

        #annual bonus method and summery afterward
        print(f"Annual bonus: {employee_obj.annual_bonus()}")
        print("-----SUMMARY-----")
        print(employee_obj)

        #skips the rest of the code which is for the Manager subclass
        continue

    #manager object scope
    try:
        team_size = int(input("Enter the number of the team: "))
        manager_obj = Manager(name, salary, team_size)
    #error handling for creating the object
    except ValueError as e:
        print(e)
        continue

    print(f"Annual bonus: {manager_obj.annual_bonus()}")
    print("-----SUMMARY-----")
    print(manager_obj)