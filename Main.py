#==========LIBRARIES==========
from EduSysManager import EduSysManager
from Student import Student
from Subject import Subject
from Analytics import Analytics

#==========FLOW FUNCTIONS==========
def add_subject():
    while True:
        try:
            course_code = input("Enter course code (Must start with 8 digits followed by an uppercase letter and two "
                                "lowercase letter. e.g. 12345678Abc): ")
            if course_code in Subject.courses:
                raise ValueError("Invalid input. This course already exist. ")
            course_name = input("Enter course name: ")
            course_unit = input("Enter course unit: ")

            sub_obj = Subject(course_code, course_name, course_unit)
            print(sub_obj)
            print("Subject added successfully. ")
            print(f"Total subjects: {len(Subject.courses)}")
            break
        except ValueError as e:
            print(e)

def remove_subject():
    if len(Subject.courses) == 0:
        print("WARNING. There isn't any subject in the system. Please add one subject first.")
        return

    while True:
        try:
            course_code = input("Enter course code (Must start with 8 digits followed by an uppercase letter and two"
                                " lowercase letter. e.g. 12345678Abc): ")
            if course_code not in Subject.courses:
                raise ValueError("Invalid input. Course does not exist. ")
            Subject.courses.pop(course_code)
            print("Subject removed successfully. ")
            print(f"Total subjects: {len(Subject.courses)}")
            break
        except ValueError as e:
            print(e)

def compare_subjects():
    if len(Subject.courses) < 2:
        print("WARNING. There must be at least 2 subjects in the system to compare them. Please add subjects first.")
        print(f"Total subjects: {len(Subject.courses)}")
        return

    while True:
        try:
            course_code1 = input("Enter subject #1 code(Must start with 8 digits followed by an uppercase letter and two"
                                 " lowercase letter. e.g. 12345678Abc): ")
            course_code2 = input("Enter subject #2 code(Must start with 8 digits followed by an uppercase letter and two"
                                 " lowercase letter. e.g. 12345678Abc): ")
            key = input("Enter key: ")
            sub_obj1 = Subject.courses[course_code1]
            sub_obj2 = Subject.courses[course_code2]

            result = []
            if key.lower() not in ("equal", "greater or equal", "lower or equal"):
                raise ValueError("Invalid input. Comparison is only available for ('equal', 'greater or equal', 'lesser or equal'). ")

            result.append("="*55)
            if key.lower() == "equal":
                status = sub_obj1 == sub_obj2
            elif key.lower() == "greater or equal":
                status = sub_obj1 >= sub_obj2
            else:
                status = sub_obj1 <= sub_obj2

            status = "is" if status else "isn't"
            result.append(f"{sub_obj1.course_name} {status} {key} to {sub_obj2}")

            print("\n".join(result))
            break
        except (ValueError, KeyError) as e:
            print(e)

def get_all_subjects():
    print(f"Total Subjects in system: {len(Subject.courses)}")
    print("-"*55)
    for sub,sub_obj in Subject.courses.items():
        print(sub_obj)

def add_student_flow():
    if len(Subject.courses) == 0:
        print("WARNING. There isn't any subject in the system. Please add subject first.")
        return

    while True:
        try:
            first_name = input("Enter first name (Must be capitalized. e.g. Ali): ")
            last_name = input("Enter last name (Must be capitalized. e.g. Hosseini): ")
            national_id = input("Enter national ID (Must has only 11 digits. e.g. 01234567890): ")
            stu_id = input("Enter student ID (Must has only 8 digits. e.g. 12345678): ")
            degree = input("Enter degree: (Valid degrees are: 'associate', 'bachelor', 'master' or 'phd')")
            term = input("Enter term (Must be an integer): ")

            courses_code_list, stu_grades_list = [], []
            repeat = 1
            while repeat == 1:
                course_code = input("Enter code of the course that student has(Must start with 8 digits followed by "
                                    "an uppercase letter and two lowercase letter. e.g. 12345678Abc): ")
                if course_code in courses_code_list:
                    print(f"Invalid input. Student already has this course {course_code}")
                    continue

                if course_code not in Subject.courses:
                    print(f"Invalid input. Course code: {course_code} does not exist in system.")
                    continue

                stu_grade = input(f"Enter student grade in course {course_code} | "
                                  f"{Subject.courses[course_code].course_name} : ")
                try:
                    stu_grade = float(stu_grade)
                except ValueError:
                    print("Invalid input. Enter a floating point number for grade. ")
                    continue

                courses_code_list.append(course_code)
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
            EduSysManager.add_student_to_system(stu_id, stu_obj)
            print("Student added successfully. ")
            print(stu_obj)
            print(f"Total students: {EduSysManager.total_students}")
            break

        except ValueError as e:
            print(e)

def remove_student_flow():
    if len(EduSysManager.students) == 0:
        print("WARNING. There isn't any student in the system. Please add one first. ")
        return

    while True:
        try:
            stu_id = input("Enter student ID (Must has only 8 digits. e.g. 12345678): ")
            EduSysManager.remove_student_from_system(stu_id)
            print("Student removed from system successfully. ")
            print(f"Total students: {EduSysManager.total_students}")
            break
        except ValueError as e:
            print(e)

def compare_students():
    if len(EduSysManager.students) < 2:
        print("WARNING. There must be at least 2 students in the system to compare them. Please at least add 2 students.")
        return

    while True:
        try:
            stu_id1 = input("Enter student #1 ID (Must has only 8 digits. e.g. 12345678): ")
            stu_id2 = input("Enter student #2 ID (Must has only 8 digits. e.g. 12345678):")
            key = input("Enter key: ")
            stu_obj1 = EduSysManager.students[stu_id1]
            stu_obj2 = EduSysManager.students[stu_id2]

            result = []
            if key.lower() not in ("equal", "greater or equal", "lower or equal"):
                raise ValueError("Invalid input. Comparison is only available for ('equal', 'greater or equal', 'lesser or equal'). ")

            result.append("="*55)
            if key.lower() == "equal":
                status = stu_obj1 == stu_obj2
            elif key.lower() == "greater or equal":
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
    if len(Subject.courses) == 0 or len(EduSysManager.students) == 0:
        print("WARNING. To add course there must be at least one subject and student in the system. ")
        return

    while True:
        try:
            stu_id = input("Enter student ID (Must has only 8 digits. e.g. 12345678): ")
            course_code = input("Enter course code (Must start with 8 digits followed by an uppercase letter and two"
                                " lower case letter. e.g. 12345678Abc): ")
            student_grade = input("Enter student grade: ")
            try:
                student_grade = float(student_grade)
            except ValueError:
                print("Invalid input. Enter a floating point number for grade. ")
                continue

            EduSysManager.add_course(stu_id, course_code, student_grade)
            print("Course added successfully. ")
            break

        except ValueError as e:
            print(e)

def remove_course_flow():
    if len(Subject.courses) == 0 or len(EduSysManager.students) == 0:
        print("WARNING. To remove a course from a student profile, there must be at least one student and subject in the system.")
        return

    while True:
        try:
            stu_id = input("Enter student ID (Must has only 8 digits. e.g. 12345678.): ")
            course_code = input("Enter course code (Must start with 8 digits followed by an uppercase letter and two"
                                " lower case letter. e.g. 12345678Abc)")
            EduSysManager.remove_course(stu_id, course_code)
            print("Course removed successfully. ")
            break

        except ValueError as e:
            print(e)

def find_student():
    if len(EduSysManager.students) == 0:
        print("WARNING. There must be at least one student in the system to check their transcript. Please add student first.")
        return

    while True:
        try:
            basis = input("Enter basis (Finding student(s) by their 'student ID', 'first name' or 'last name') : ")
            key = input("Enter key (student ID/first name/last name of the student(s)): ")
            answer = EduSysManager.find_student(basis, key)
            print(answer)
            break

        except ValueError as e:
            print(e)

def sorted_output():
    if len(EduSysManager.students) < 2:
        print("WARNING. There must be at least two students in the system to sort them. ")
        return

    while True:
        try:
            key = input("Enter key (Sorting students by their 'gpa', 'total unit', 'first name' or 'last name'): ")
            answer = EduSysManager.sort_students(key)
            for stu_id, stu_obj in answer:
                print(stu_obj)
            break

        except ValueError as e:
            print(e)

def data_analysis():
    if len(EduSysManager.students) == 0:
        print("WARNING. There must be at least one student in the system to check statistical analysis. ")
        return

    while True:
        try:
            basis = input("Enter basis (Statistical analysis on students based on 'all', 'course', 'term', 'degree'): ")
            key = input("Enter key (Students in which course/term/degree. for all, just skip.): ")
            analysis = Analytics()
            answer = analysis.get_stats(basis, key)
            print(answer)
            break

        except ValueError as e:
            print(e)

#==========MAIN SCOPE==========
operation_table = {"1":("get all subjects", get_all_subjects),
                   "2": ("add subject to the system", add_subject),
                   "3": ("remove subject from the system", remove_subject),
                   "4": ("compare two subjects by their unit", compare_subjects),
                   "5": ("add student to the system", add_student_flow),
                   "6": ("remove student from the system", remove_student_flow),
                   "7": ("compare two students by their GPA", compare_students),
                   "8": ("add course to the student profile", add_course_flow),
                   "9": ("remove course from student profile", remove_course_flow),
                   "10": ("find student(s) transcript", find_student),
                   "11": ("sort students", sorted_output),
                   "12": ("statistical analysis on students' grade", data_analysis)}
while True:
    print("="*55)
    for order, (label, _) in operation_table.items():
        print(f"{order}. {label}")
    print("0. exit")

    choice = input("Enter choice: ")
    if choice == "0":
        break

    elif choice in operation_table:
        try:
            operation_table[choice][1]()
        except (ValueError, KeyError) as er:
            print(er)
    else:
        print("Invalid input. Input must be a number from 0 to 12. ")