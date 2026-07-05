from EduSysManager import EduSysManage
from Student import Student
from Subject import Subject
from Analytics import Analytics

def add_subject():
    while True:
        try:
            course_code = input("Enter course code: ")
            if course_code in Subject.courses:
                raise ValueError("Invalid input. This course already exist. ")
            course_name = input("Enter course name: ")
            course_unit = input("Enter course unit: ")

            sub_obj = Subject(course_code, course_name, course_unit)
            print(sub_obj)
            print("Subject added successfully. ")
            break
        except ValueError as e:
            print(e)

def remove_subject():
    while True:
        try:
            course_code = input("Enter course code: ")
            if course_code not in Subject.courses:
                raise ValueError("Invalid input. Course does not exist. ")
            Subject.courses.pop(course_code)
            print("Subject removed successfully. ")
            break
        except ValueError as e:
            print(e)

def compare_subjects():
    while True:
        try:
            course_code1 = input("Enter subject #1 code: ")
            course_code2 = input("Enter subject #2 code: ")
            key = input("Enter key: ")
            sub_obj1 = Subject.courses[course_code1]
            sub_obj2 = Subject.courses[course_code2]

            result = []
            if key.lower() not in ("equal", "greater or equal", "lower or equal"):
                raise ValueError("Invalid input. Comparison is only available for ('equal', 'greater or equal', 'lesser or equal'). ")

            result.append("="*55)
            if key == "equal":
                status = sub_obj1 == sub_obj2
            elif key == "greater or equal":
                status = sub_obj1 >= sub_obj2
            else:
                status = sub_obj1 <= sub_obj2

            status = "is" if status else "isn't"
            result.append(f"{sub_obj1.course_name} {status} {key} to {sub_obj2}")

            print("\n".join(result))
            break
        except (ValueError, KeyError) as e:
            print(e)


def add_student_flow():
    while True:
        try:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            national_id = input("Enter national ID: ")
            stu_id = input("Enter student ID: ")
            degree = input("Enter degree: ")
            term = input("Enter term: ")

            courses_code_list, stu_grades_list = [], []
            repeat = 1
            while repeat == 1:
                course_code = input("Enter course code: ")
                courses_code_list.append(course_code)
                stu_grade = input(f"Enter student grade in course {course_code}: ")
                try:
                    stu_grade = float(stu_grade)
                except ValueError:
                    print("Invalid input. Enter a floating point number for grade. ")
                    continue
                stu_grades_list.append(stu_grade)

                try:
                    repeat = int(input("Enter \n\t0. exit adding course. "
                                       "\n\t1. add another course. \n"))
                    if repeat not in (0 ,1):
                        print("Invalid input. Enter 1 or 2. ")
                        continue

                except ValueError:
                    print("Invalid input. Enter 1 or 2.")

            stu_obj = Student(first_name, last_name, national_id, stu_id, degree, term, courses_code_list, stu_grades_list)
            EduSysManage.add_student_to_system(stu_id, stu_obj)
            print(stu_obj)
            print( "Student added successfully. ")
            break

        except ValueError as e:
            print(e)

def remove_student_flow():
    while True:
        try:
            stu_id = input("Enter student ID: ")
            EduSysManage.remove_student_from_system(stu_id)
            print("Student removed from system successfully. ")
            break
        except ValueError as e:
            print(e)

def compare_students():
    while True:
        try:
            stu_id1 = input("Enter student #1 ID: ")
            stu_id2 = input("Enter student #2 ID:")
            key = input("Enter key: ")
            stu_obj1 = EduSysManage.students[stu_id1]
            stu_obj2 = EduSysManage.students[stu_id2]

            result = []
            if key.lower() not in ("equal", "greater or equal", "lower or equal"):
                raise ValueError("Invalid input. Comparison is only available for ('equal', 'greater or equal', 'lesser or equal'). ")

            result.append("="*55)
            if key == "equal":
                status = stu_obj1 == stu_obj2
            elif key == "greater or equal":
                status = stu_obj1 >= stu_obj2
            else:
                status = stu_obj1 <= stu_obj2

            status = "is" if status else "isn't"
            result.append(f"{stu_obj1.l_name} {stu_obj1.f_name} GPA {status} {key} to {stu_obj2.l_name} {stu_obj2.f_name}. ")
            print("\n".join(result))
            break
        except (ValueError, KeyError) as e:
            print(e)

def add_course_flow():
    while True:
        try:
            stu_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            student_grade = input("Enter student grade: ")
            try:
                student_grade = float(student_grade)
            except ValueError:
                print("Invalid input. Enter a floating point number for grade. ")
                continue
            EduSysManage.add_course(stu_id, course_code, student_grade)
            print("Course added successfully. ")
            break

        except ValueError as e:
            print(e)

def remove_course_flow():
    while True:
        try:
            stu_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            EduSysManage.remove_course(stu_id, course_code)
            print("Course removed successfully. ")
            break

        except ValueError as e:
            print(e)

def find_student():
    while True:
        try:
            basis = input("Enter basis: ")
            key = input("Enter key: ")
            answer = EduSysManage.find_student(basis, key)
            print(answer)
            break

        except ValueError as e:
            print(e)

def sorted_output():
    while True:
        try:
            key = input("Enter key: ")
            answer = EduSysManage.sort_students(key)
            for stu_id, stu_obj in answer:
                print(stu_obj)
            break

        except ValueError as e:
            print(e)

def data_analysis():
    while True:
        try:
            basis = input("Enter basis: ")
            key = input("Enter key: ")
            analysis = Analytics()
            answer = analysis.get_stats(basis, key)
            print(answer)
            break

        except ValueError as e:
            print(e)