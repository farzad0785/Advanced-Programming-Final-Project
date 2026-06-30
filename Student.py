from Person import Person
import MyFunctions
from Subject import Subject

class Student(Person):
    total_students = 0
    def __init__(self, first_name, last_name, national_id, stu_id, degree, term, courses_code_list, stu_grades_list, ):
        super().__init__(first_name, last_name, national_id)
        self._gpa = None
        self._student_courses = None
        self._total_unit = None
        self.stu_id = stu_id
        self.stu_courses_code = courses_code_list
        self.stu_grades = stu_grades_list
        self.degree = degree
        self.term = term
        Student.total_students += 1

    #==========PROPERTIES AND SETTERS==========
    @property
    def stu_id(self):
        return self._stu_id
    @stu_id.setter
    def stu_id(self, new_id):
        if not MyFunctions.is_digits(new_id, 8):
            raise ValueError("Invalid input. Student ID must be only 8 digits. ")
        self._stu_id = new_id

    @property
    def stu_courses_code(self):
        return self._stu_courses_code
    @stu_courses_code.setter
    def stu_courses_code(self, courses_code_list):
        for course in courses_code_list:
            if course not in Subject.courses:
                raise ValueError("Invalid input. Course does not exist. ")
        self._stu_courses_code = courses_code_list

    @property
    def stu_grades(self):
        return self._stu_grades
    @stu_grades.setter
    def stu_grades(self, grades_list):
        for grade in grades_list:
            if 0 > grade or grade > 20:
                raise ValueError("Invalid input. Grade cannot be negative or greater than 20.")
        self._stu_grades = grades_list

    @property
    def degree(self):
        return self._degree
    @degree.setter
    def degree(self, new_degree):
        if new_degree.lower() not in ("associate","bachelor", "master", "phd"):
            raise ValueError("Invalid input. Degrees can be 'bachelor', 'master' or 'phd'.")
        self._degree = new_degree

    @property
    def term(self):
        return self._term
    @term.setter
    def term(self, new_term):
        try:
            self._term = int(new_term)
        except ValueError:
            raise ValueError("Invalid input. Student term must be an integer. ")

    @property
    def gpa(self):
        total_grade_and_unit, self._total_unit = 0,0
        for course_code, grade in self._student_courses.items():
            total_grade_and_unit += grade * Subject.courses[course_code]["unit"]
        for course_code in self.stu_courses_code:
            self._total_unit += Subject.courses[course_code]
        self._gpa = total_grade_and_unit / self._total_unit
        return self._gpa

    #==========METHODS==========
    def student_courses(self):
        self._student_courses = dict(zip(self.stu_courses_code, self.stu_grades))
        return self._student_courses

    def add_course(self, course_code, grade):
        if course_code not in Subject.courses:
            raise ValueError("Invalid input. Entered course does not exist. ")
        elif course_code in self.stu_courses_code:
            raise ValueError("Invalid input. Student already has this course. ")
        self._student_courses.append(course_code)
        self._student_courses[course_code] = grade

    def remove_course(self, course_name):
        if course_name not in self.stu_courses_code:
            raise ValueError("Invalid input. Student does not have this course. ")
        self.stu_courses_code.pop(course_name)
        self._student_courses.pop(course_name)

    def course_pass_check(self):
        for course,grade in self._student_courses.items():
            if grade < 10:
                print(f"Student has failed course: {course} | Grade: {grade}")
            else:
                print(f"Student has passed course: {course} | Grade: {grade}")

    def term_pass_check(self):
        if self.degree == "associate" or self.degree == "bachelor":
            if self.gpa < 12:
                print("Student has failed. ")
                return False
            else:
                print("Student has passes. ")
                return True

        elif self.degree == "master":
            if self.gpa < 14:
                print("Student has failed. ")
                return False
            else:
                print("Student has passes. ")
                return True

        else:
            if self.gpa < 16:
                print("Student has failed. ")
                return False
            else:
                print("Student has passes. ")
                return True

    def __str__(self):
        return (f"Student ID: {self.stu_id} "
                f"Last name: {Person.l_name} | First name: {Person.f_name} "
                f"National ID: {Person.national_id} "
                f"Degree: {self.degree} | Term: {self.term}"
                f"Total unit: {self._total_unit} | gpa: {self.gpa}"
                f"Pass/Fail: {self.term_pass_check()}" )

    def __ge__(self, other):
        return self.gpa >= other.gpa
    def __eq__(self, other):
        return self.gpa == other.gpa
    def __le__(self, other):
        return self.gpa <= other.gpa
