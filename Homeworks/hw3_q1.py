#Name: Aliasghar Rashidabadi
#Course: Advanced Programming
#Student ID: 40419533

import csv

with open('std_info_4042.txt', 'r') as f:
    csv_reader = csv.reader(f)
    field_names = next(csv_reader)

    with open('std_info_4042.csv', 'w', newline="") as file:
        csv_writer = csv.DictWriter(file, fieldnames=field_names)
        csv_writer.writeheader()
        students = []

        for row in csv_reader:
            data = dict(zip(field_names, row))
            students.append(data)

        csv_writer.writerows(students)

        #similar output like the example
        #print(students)