#156 178 165 171 187
students_height = input("Input a list of students heights\n").split()
count = 0
sum = 0

for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])

for height in students_height:
   sum += height
for item in students_height:
    count += 1
print(sum)
print(count)
Average = round(sum / count)
print(Average)



