marks = [
    [80, 75, 90],
    [60, 55, 70],
    [95, 85, 92]
]


for i in range(len(marks)):
    total = sum(marks[i])
    average = total / len(marks[i])

    print("Student", i + 1, "total:", total)
    print("Student", i + 1, "average:", average)

for subject in range(3):
    total = 0

    for student in range(len(marks)):
        total = total + marks[student][subject]

    average = total / len(marks)

    print("Subject", subject + 1, "average:", average)

    if average < 60:
        print("This subject has a low average.")
