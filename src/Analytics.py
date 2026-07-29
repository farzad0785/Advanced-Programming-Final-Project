import numpy as np
from EduSysManager import EduSysManager

class Analytics(object):
    def __init__(self):
        self.system = EduSysManager

    def all_grades_np(self, basis, key):
        if basis.lower() not in ("all", "degree", "major", "term", "course"):
            raise ValueError("Invalid input. statistical is only available for ('all', 'major', 'degree', "
                             "'term' and 'course')")
        all_grades = []

        if basis.lower() == "degree":
            for student in self.system.students.values():
                if student.degree == key.capitalize():
                    all_grades.extend(student.stu_grades)

        elif basis.lower() == "major":
            for student in self.system.students.values():
                if student.major == key.capitalize():
                    all_grades.extend(student.stu_grades)

        elif basis.lower() == "term":
            for student in self.system.students.values():
                if student.term == int(key):
                    all_grades.extend(student.stu_grades)

        elif basis.lower() == "course":
            for student in self.system.students.values():
                for course, grade in student.get_grades().items():
                    if course == key.capitalize():
                        all_grades.append(grade)


        else:
            for student in self.system.students.values():
                all_grades.extend(student.stu_grades)

        return np.array(all_grades, dtype=np.float32)

    def get_stats(self, basis, key):
        grades_array = self.all_grades_np(basis, key)
        if len(grades_array) == 0:
            raise ValueError("Invalid input. No grades found for the entered filter. ")

        result = []
        key_str = key if key else "all students"
        result.append("="*55)
        result.append(f"Statistical analysis for grades based on {basis}: {key_str}")
        result.append(f"Max grade: {grades_array.max()}")
        result.append(f"Min grade: {grades_array.min()}")
        result.append(f"Mean grade: {grades_array.mean()}")
        result.append(f"Std grade: {grades_array.std()}")
        result.append("-"*55)
        result.append(f"Passed grades: {np.sum(10 <= grades_array)}")
        result.append(f"Failed grades: {np.sum(10 > grades_array)}")
        result.append("="*55)

        return "\n".join(result)