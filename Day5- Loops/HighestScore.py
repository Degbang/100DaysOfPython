students_scores = input("Input a list of students scores\n").split()

for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])
# print(students_scores)
highest_score = 0
for score in students_scores:
    if score > highest_score:
        highest_score = score
print(f"{highest_score} is the highest")
