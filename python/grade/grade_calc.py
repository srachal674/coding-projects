test_scores = []

for g in range (3):
    grade = int(input(f"Enter test grade{g+1}: "))
    test_scores.append(grade)

test_ave = sum(test_scores)/3

project = int(input(f"Enter project grade: "))

homework_ave = int(input(f"Enter homework grade: "))

# Calculate the total weighted grade
test_points = test_ave * 0.50
project_points = project * 0.30
homework_points = homework_ave * 0.20

total_score = test_points + project_points + homework_points

test_ave = sum(test_scores) / 3
test_weighted = test_ave * .50

# determine letter grade
if total_score >= 90:
    letter = "A"
elif total_score >= 80:
    letter = "B"
elif total_score >= 70:
    letter = "C"
elif total_score >= 60:
    letter = "D"
else:
    letter = "F"

# print both together
print(f"Final Grade: {round(total_score)}% ({letter})")