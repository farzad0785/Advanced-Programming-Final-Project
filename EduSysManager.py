from Utils import merge_sort

class EduSysManage(object):
    students = {}
    total_students = 0

    @staticmethod
    def add_student_to_system(stu_id, stu_obj):
        if stu_id in EduSysManage.students:
            raise ValueError("Invalid input. Student already exist. ")
        EduSysManage.students[stu_id] = stu_obj
        EduSysManage.total_students += 1

    @staticmethod
    def remove_student_from_system(stu_id):
        if stu_id not in EduSysManage.students:
            raise ValueError("Invalid input. Student does not exist. ")
        EduSysManage.students.pop(stu_id)
        EduSysManage.total_students -= 1

    @staticmethod
    def add_course(stu_id, course_code, stu_grade):
        if stu_id not in EduSysManage.students:
            raise ValueError("Invalid input. Student does not exist. ")

        stu_obj = EduSysManage.students[stu_id]
        stu_obj.add_course(course_code, stu_grade)

    @staticmethod
    def remove_course(stu_id, course_code):
        if stu_id not in EduSysManage.students:
            raise ValueError("Invalid input. Student does not exist. ")

        stu_obj = EduSysManage.students[stu_id]
        stu_obj.remove_course(course_code)

    @staticmethod
    def find_student(basis, key):
        """Finds a particular student(s) by their student ID or
        first/last name in the system. Returned value is their transcript. """
        if basis.lower() not in ("student id", "first name", "last name"):
            raise ValueError("Invalid input. Finding student is only available with student ID, first/last name. ")
        stu_obj = {}
        result = []
        if basis.lower() == "student id":
            if key in EduSysManage.students:
                stu_obj[key] = EduSysManage.students[key]

        elif basis.lower() == "first name":
            for stu_id, student in EduSysManage.students.items():
                if key == student.f_name:
                    stu_obj[stu_id] = student

        else:
            for stu_id, student in EduSysManage.students.items():
                if key == student.l_name:
                    stu_obj[stu_id] = student

        if not stu_obj:
            raise ValueError("Invalid input. Student does not exist. ")

        for stu_id, student_obj in stu_obj.items():
            result.append(student_obj.show_transcript())

        return "\n".join(result)

    @staticmethod
    def sort_students(choice):
        """returns sorted student based on their choice. """
        result = []
        students_list = list(EduSysManage.students.items())
        result.append(merge_sort(students_list, choice))

        return "\n".join(result)