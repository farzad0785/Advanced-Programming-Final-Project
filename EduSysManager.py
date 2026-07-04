from Student import Student
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
    def find_student(stu_id):
        """Finds a particular student in the system and returns their transcript. """
        if stu_id not in EduSysManage.students:
            raise ValueError("Invalid input. Student does not exist. ")

        stu_obj = EduSysManage.students[stu_id]
        return stu_obj.show_transcript()

    @staticmethod
    def sort_students(choice):
        """returns sorted student based on their choice. """
        students_list = list(EduSysManage.students.items())
        sorted_students = merge_sort(students_list, choice)
        result = []
        #Needs formation
        for student in sorted_students:
            result.append(student)
        return "\n".join(result)