grades_sum = gpa = least_diff = count = 0
path = "C://beta/alpha.dat"
output_path = "C://beta/alpha_updated.dat"
with open(path, "r") as f:
    for grade in f:
        grades_sum += float(grade.strip())
        count += 1

gpa = grades_sum/count
least_diff = float("inf")

with open(path, "r") as f:
    for grade in f:
        if least_diff >= abs(gpa - float(grade.strip())):
            least_diff = abs(gpa - float(grade.strip()))

with open(output_path, "w") as f_output:
    with open(path, "r") as f_input:

        f.write(f"GPA: {gpa:.2f} \n")
        for grade in f_input:
            if abs(float(grade.strip()) - gpa) == least_diff:
                f_output.write(f"{grade.strip()} *\n")
            else:
                f_output.write(f"{grade.strip()}")
            f_output.write("-" * 15 + "\n")
