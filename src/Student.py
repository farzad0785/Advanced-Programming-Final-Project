import Utils
from Person import Person
from Subject import Subject
from Major import Major

class Student(Person):
    def __init__(self, first_name, last_name, national_id, stu_id, degree, major,
                 term, courses_code_list, stu_grades_list):
        super().__init__(first_name, last_name, national_id)
        self._gpa = None
        self._student_courses = {}
        self.stu_id = stu_id
        self.stu_courses_code = courses_code_list
        self.stu_grades = stu_grades_list
        self.degree = degree
        self.major = major
        self.term = term
        self._build_student_courses()

    #==========PROPERTIES AND SETTERS==========
    @property
    def stu_id(self):
        return self._stu_id
    @stu_id.setter
    def stu_id(self, new_id):
        if not Utils.is_digits(new_id, 8):
            raise ValueError("Invalid input. Student ID must be only 8 digits. ")
        self._stu_id = new_id

    @property
    def stu_courses_code(self):
        return self._stu_courses_code
    @stu_courses_code.setter
    def stu_courses_code(self, courses_code_list):
        for course_code in courses_code_list:
            if course_code not in Subject.courses:
                raise ValueError(f"Invalid input. Course code: {course_code} does not exist. ")
        self._stu_courses_code = courses_code_list

    @property
    def stu_grades(self):
        return self._stu_grades
    @stu_grades.setter
    def stu_grades(self, grades_list):
        for grade in grades_list:
            if grade < 0 or grade > 20:
                raise ValueError("Invalid input. Grade cannot be negative or greater than 20.")
        self._stu_grades = grades_list

    @property
    def degree(self):
        return self._degree
    @degree.setter
    def degree(self, new_degree):
        if new_degree not in ("Associate","Bachelor", "Master", "Phd"):
            raise ValueError("Invalid input. Degree must be among 'Associate', 'Bachelor', 'Master' or 'Phd'.")
        self._degree = new_degree

    @property
    def major(self):
        return self._major
    @major.setter
    def major(self, new_major):
        if new_major not in Major.all_majors:
            raise ValueError(f"Invalid input. {new_major} does not exist. ")
        self._major = new_major

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
    def total_unit(self):
        return sum(Subject.courses[course_code].course_unit for course_code in self._student_courses)

    @property
    def gpa(self):
        total_weighted, total_unit = 0, 0

        for course_code, grade in self._student_courses.items():
            unit = Subject.courses[course_code].course_unit
            total_weighted += grade * unit
            total_unit += unit

        self._gpa = total_weighted / total_unit if total_unit > 0 else 0
        return self._gpa

    #==========METHODS==========
    def _build_student_courses(self):
        if len(self.stu_courses_code) != len(self.stu_grades):
            raise ValueError("Invalid input. Number of courses and grades does not match. ")
        self._student_courses = dict(zip(self.stu_courses_code, self.stu_grades))

    def get_grades(self):
        """Public method to access the protected attribute. """
        return self._student_courses

    def add_course(self, course_code, course_grade):
        if course_code not in Subject.courses:
            raise ValueError("Invalid input. Entered course does not exist. ")
        elif course_code in self.stu_courses_code:
            raise ValueError("Invalid input. Student already has this course. ")
        elif course_grade < 0 or 20 < course_grade:
            raise ValueError("Invalid input. Student grade cannot be negative or greater than 20. ")

        self._student_courses[course_code] = course_grade
        self.stu_courses_code.append(course_code)
        self.stu_grades.append(course_grade)

    def remove_course(self, course_name):
        if course_name not in self.stu_courses_code:
            raise ValueError("Invalid input. Student does not have this course. ")

        idx = self.stu_courses_code.index(course_name)
        self.stu_grades.pop(idx)
        self.stu_courses_code.remove(course_name)
        self._student_courses.pop(course_name)

    def course_pass_check(self):
        result = []
        result.append(f"{'Code':<12} {'Name':<20} {'Grade':<6} {'Unit':<6} {'Status':<8}")

        for course_code,grade in self._student_courses.items():
            status = "PASS"
            if grade < 10:
                status = "FAIL"
            course_info = Subject.courses[course_code]
            result.append(f"{course_code:<12} {course_info.course_name:<20} {grade:<6} "
                  f"{course_info.course_unit:<6} {status:<8}")
        return "\n".join(result)

    def term_pass_check(self):
        if self.degree in ("Associate", "Bachelor"):
            return self.gpa >= 12
        elif self.degree == "Master":
            return self.gpa >= 14
        else:
            return self.gpa >= 16

    def show_transcript(self):
        result = []
        result.append("="*55)
        result.append(f"TRANSCRIPT FOR: {self.l_name} {self.f_name}")

        result.append("-"*55)
        result.append(f"Student ID: {self.stu_id} | National ID: {self.national_id}")

        result.append("-"*55)
        result.append(f"Degree: {self.degree} | Major: {self.major} | Term: {self.term}")

        result.append("-"*55)
        result.append(self.course_pass_check())

        result.append(f"GPA: {self.gpa:.2f} | Total unit: {self.total_unit}")
        status = "PASSED" if self.term_pass_check() else "FAILED"
        result.append(f"STATUS: {status}")

        return "\n".join(result)

    #==========DUNDER METHODS==========
    def __str__(self):
        return (f"Last name: {self.l_name} | First name: {self.f_name}"
                f"\nStudent ID: {self.stu_id} | National ID: {self.national_id}"
                f"\nDegree: {self.degree} | Major: {self.major} | Term: {self.term}"
                f"\nGPA: {self.gpa:.2f} | Total unit: {self.total_unit}")

    def __ge__(self, other):
        return self.gpa >= other.gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __le__(self, other):
        return self.gpa <= other.gpa
