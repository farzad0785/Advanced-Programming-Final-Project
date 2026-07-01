import MyFunctions
class Subject(object):
    courses = {}
    def __init__(self, course_code, course_name, course_unit):
        self.course_code = course_code
        self.course_name = course_name
        self.course_unit = course_unit
        Subject.courses[course_code] = {
            "course name": course_name,
            "course unit": course_unit,
        }

    #==========PROPERTIES AND SETTERS==========
    @property
    def course_code(self):
        return self._course_code
    @course_code.setter
    def course_code(self, new_code):
        if not MyFunctions.is_digits(new_code, 10):
            raise ValueError("Invalid input. Course code must have only 10 digits. ")
        self._course_code = new_code

    @property
    def course_name(self):
        return self._course_name
    @course_name.setter
    def course_name(self, new_name):
        Subject.courses[self.course_code]["course name"] = new_name
        self._course_name = new_name

    @property
    def course_unit(self):
        return self._course_unit
    @course_unit.setter
    def course_unit(self, new_unit):
        try:
            self._course_unit = int(new_unit)
            Subject.courses[self.course_code]["unit"] = self._course_unit
        except ValueError:
            raise ValueError("Invalid input. Course unit must be an integer.")

    #==========METHODS==========