class Subject(object):
    courses = {}
    def __init__(self, course_code, course_name, course_unit, stu_list, stu_grade):
        self.course_code = course_code
        self.course_name = course_name
        self.course_unit = course_unit
        self.stu_list = []
        Subject.courses[course_code] = {course_name: course_unit}
