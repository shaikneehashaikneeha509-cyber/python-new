answer_key = ["A", "C", "B", "D"]
students = [
    ["A", "C", "D", "D"],
    ["A", "", "B", "C"]
]

for number in range(len(students)):
    correct = 0
    incorrect = 0
    unanswered = 0

    for i in range(len(answer_key)):
        answer = students[number][i]

        if answer == "":
            unanswered = unanswered + 1
        elif answer == answer_key[i]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1

    score = correct - (incorrect * 0.25)

    print("Student", number + 1)
    print("Correct:", correct)
    print("Incorrect:", incorrect)
    print("Unanswered:", unanswered)
    print("Score:", score)
