import Utils

class Subject(object):
    courses = {}
    def __init__(self, course_code, course_name, course_unit):
        self.course_code = course_code
        self.course_name = course_name
        self.course_unit = course_unit
        Subject.courses[course_code] = self

    #==========PROPERTIES AND SETTERS==========
    @property
    def course_code(self):
        return self._course_code
    @course_code.setter
    def course_code(self, new_code):
        if not Utils.is_course_code_valid(new_code):
            raise ValueError("Invalid input. Course code must have 8 digits, followed by an uppercase and 2 lower case letters.")
        self._course_code = new_code

    @property
    def course_name(self):
        return self._course_name
    @course_name.setter
    def course_name(self, new_name):
        self._course_name = new_name.capitalize()

    @property
    def course_unit(self):
        return self._course_unit
    @course_unit.setter
    def course_unit(self, new_unit):
        try:
            self._course_unit = int(new_unit)
        except ValueError:
            raise ValueError("Invalid input. Course unit must be an integer.")

    #==========DUNDER METHODS==========
    def __str__(self):
        return f"Course code: {self.course_code} | Course name: {self.course_name} | Course unit: {self.course_unit}"
    def __eq__(self, other):
        return self.course_unit == other.course_unit
    def __ge__(self, other):
        return self.course_unit >= other.course_unit
    def __le__(self, other):
        return self.course_unit <= other.course_unit