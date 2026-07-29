from Utils import merge_sort

class EduSysManager(object):
    students = {}
    total_students = 0

    #=====STATIC METHODS==========
    @staticmethod
    def add_student_to_system(stu_id, stu_obj):
        if stu_id in EduSysManager.students:
            raise ValueError("Invalid input. Student already exist. ")
        EduSysManager.students[stu_id] = stu_obj
        EduSysManager.total_students += 1

    @staticmethod
    def remove_student_from_system(stu_id):
        if stu_id not in EduSysManager.students:
            raise ValueError("Invalid input. Student does not exist. ")
        EduSysManager.students.pop(stu_id)
        EduSysManager.total_students -= 1

    @staticmethod
    def add_course(stu_id, course_code, stu_grade):
        if stu_id not in EduSysManager.students:
            raise ValueError("Invalid input. Student does not exist. ")

        stu_obj = EduSysManager.students[stu_id]
        stu_obj.add_course(course_code, stu_grade)

    @staticmethod
    def remove_course(stu_id, course_code):
        if stu_id not in EduSysManager.students:
            raise ValueError("Invalid input. Student does not exist. ")

        stu_obj = EduSysManager.students[stu_id]
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
            if key in EduSysManager.students:
                stu_obj[key] = EduSysManager.students[key]

        elif basis.lower() == "first name":
            for stu_id, student in EduSysManager.students.items():
                if key == student.f_name:
                    stu_obj[stu_id] = student

        else:
            for stu_id, student in EduSysManager.students.items():
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
        students_list = list(EduSysManager.students.items())
        result = (merge_sort(students_list, choice))

        return result