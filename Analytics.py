import numpy as np
from EduSysManager import EduSysManage
from Subject import Subject

class Analytics(object):
    def __init__(self):
        self.system = EduSysManage

    def all_grades_np(self):
        all_grades = []
        for stu_id, student in self.system.students.items():
            for course_code, stu_grade in student._student_course.items():
                all_grades.append(stu_grade)
        return np.array(all_grades)

    def course_analysis(self, course_code):
        pass
