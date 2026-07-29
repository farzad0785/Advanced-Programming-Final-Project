from Utils import is_capitalized

class Major:
    all_majors = []

    #==========STATIC METHODS==========
    @staticmethod
    def add_major(major):
        if not is_capitalized(major):
            raise ValueError("Invalid input. Major must be capitalized. ")
        if major in Major.all_majors:
            raise ValueError(f"Invalid input. Major {major} already exist.")
        Major.all_majors.append(major.capitalize())

    @staticmethod
    def print_all_majors():
        print(f"Total majors: {len(Major.all_majors)}")
        for major in Major.all_majors:
            print(major)