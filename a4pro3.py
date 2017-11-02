import csv
import matplotlib.pyplot as plt

names = []
grades = []

with open('a4grades.csv', newline='') as csvfile:
	students = csv.DictReader(csvfile)
	for student in students:
		names.append(student["Name"])
		grades.append(student["Grade"])

x = range(len(names))
plt.xlabel("Names")
plt.ylabel("Grades")
plt.axis([0, len(names), 0, 100])
plt.xticks(x, names, rotation="vertical")
plt.plot(x, grades, "ro")
plt.show()
