attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))

if attended < 0 or total <= 0 or attended > total:
    print("Invalid input")
else:
    percentage = (attended / total) * 100
    print("Attendance percentage:", percentage, "%")

    future = 0

    while percentage < 75:
        attended = attended + 1
        total = total + 1
        future = future + 1
        percentage = (attended / total) * 100

    print("Classes needed:", future)
