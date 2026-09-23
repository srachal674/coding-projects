# 1) How many tests?
num_scores = int(input("How many tests do you need to enter? "))

if num_scores <= 0:
    print("You must enter at least 1 test.")
    raise SystemExit

# 2) Get category max points (the slice of the 100-point total)
# Example: Tests 50, Project 30, Homework 20
test_max = float(input("Enter max point value for tests (e.g., 50): "))
project_max = float(input("Enter max point value for project (e.g., 30): "))
homework_max = float(input("Enter max point value for homework (e.g., 20): "))

total_max = test_max + project_max + homework_max

if total_max != 100:
    print(f"Your point values add to {total_max:.0f}, not 100. Try again.")
    raise SystemExit

# 3) Gather test scores
test_scores = []
for i in range(num_scores):
    grade = float(input(f"Enter test grade {i+1}: "))
    test_scores.append(grade)

test_ave = sum(test_scores) / num_scores

# 4) Get project + homework grades
project = float(input("Enter project grade: "))
homework = float(input("Enter homework grade: "))

# 5) Convert each category to its point slice out of 100
test_points = test_ave * (test_max / 100)
project_points = project * (project_max / 100)
homework_points = homework * (homework_max / 100)

total_score = test_points + project_points + homework_points

# 6) Letter grade from final total (0–100 scale)
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

print(f"Final Grade: {round(total_score)}% ({letter})")