#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

#Used for valid ID input check
import re

class Employee(object):
    total_employees = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        Employee.total_employees += 1


    def compute_salary(self):
        raise NotImplementedError("Not defined. ")

class Manager(Employee):
    total_valid_managers = 0
    total_invalid_managers = 0
    monthly_salary = 4000

    def __init__(self,name, id):
        super().__init__(name, id)
        Manager.total_valid_managers += 1

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if not Manager.is_valid_id(id):
            Manager.total_invalid_managers += 1
            raise ValueError("Manager's IDs must start with the letter 'M' followed by exactly 3 digits. ")
        self._id = id

    def compute_salary(self):
        return Manager.monthly_salary

    def __str__(self):
        return f"Manager name: {self.name}, {self.name}'s salary: {self.compute_salary()}$"

    @staticmethod
    def is_valid_id(man_id):
        #Valid ID check for managers.
        return re.fullmatch(r"M\d{3}", man_id) is not None

class Developers(Employee):
    total_valid_developers = 0
    total_invalid_developers = 0
    hourly_salary = 25
    default_worktime = 160

    def __init__(self,name, id, worktime=default_worktime):
        super().__init__(name, id)
        self.worktime = worktime
        Developers.total_valid_developers += 1

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if not Developers.is_valid_id(id):
            Developers.total_invalid_developers += 1
            raise ValueError("Developer's ID must start with the letter 'D' followed by exactly 3 digits. ")
        self._id = id

    @property
    def worktime(self):
        return self._worktime
    @worktime.setter
    def worktime(self, new_worktime):
        if new_worktime > 160:
            raise ValueError("Developers work 160 hours at most. ")
        self._worktime = new_worktime

    @staticmethod
    def is_valid_id(dev_id):
        #Valid ID check for developers.
        return re.fullmatch(r"D\d{3}", dev_id) is not None

    def compute_salary(self):
        return Developers.hourly_salary * self.worktime

    def __str__(self):
        return f"Developer's name: {self.name}, Salary: {self.compute_salary()}$, Work-time: {self.worktime}"

    #=====MAIN SCOPE=====
print("Creating valid manager and developer objects: ")
print('man1 = Manager("John", "M417")')
man1 = Manager("John", "M417")
print('dev1 = Developers("Alice", "D803")')
dev1 = Developers("Alice", "D803", 100)
print("Success")

#Seperator
print('='*20)

print("Creating invalid objects: ")
try:
    print('man2 = Manager("John", "M41")')
    man2 = Manager("John", "M41")
except ValueError as e:
    print(e)
try:
    print('dev1 = Developers("Alice", "A803")')
    dev2 = Developers("Alice", "A803")
except ValueError as e:
    print(e)

#seperator
print("="*20)
print("Employees' info: ")
employees = [man1, dev1]
for i in employees:
    print(i)
    print("="*20)

print("Employees' summaries: ")
print("Total employees:", Employee.total_employees)
print("Total valid managers:", Manager.total_valid_managers , "\b, Total invalid managers:", Manager.total_invalid_managers)
print("Total valid developers:", Developers.total_valid_developers, "\b, Total invalid developers:", Developers.total_invalid_developers)
print("="*20)
print("End of the test case")
