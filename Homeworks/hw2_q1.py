def write_in_file(year, points):
    name = input("Enter student's name: ")
    gpa = sum(int(j) for j in points)/3

    with open(f"{year}.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Lesson 1 grade: {points[0]}\n")
        f.write(f"Lesson 2 grade: {points[1]}\n")
        f.write(f"Lesson 3 grade: {points[2]}\n")
        f.write(f"GPA: {gpa:.2f}\n")
        f.write("-" * 15 + "\n")

n = int(input("Students amount: "))

for _ in range(n):
    entrance_year = int(input("Enter student's entrance year: "))

    if entrance_year not in [1400, 1401]:
        print("Invalid year. Entrance year must be 1400 or 1401")
        continue

    grades = []
    for i in range(1, 4):
        grades.append(input(f"Enter student's grade {i}: "))

    write_in_file(entrance_year, grades)