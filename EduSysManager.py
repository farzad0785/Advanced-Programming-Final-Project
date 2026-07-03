from Student import Student

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
    def find_student(stu_id):
        if stu_id not in EduSysManage.students:
            raise ValueError("Invalid input. Student does not exist. ")

        stu_obj = EduSysManage.students[stu_id]
        return stu_obj.show_transcript()
    