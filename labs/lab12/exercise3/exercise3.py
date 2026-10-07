grade = float(input())
total_grade = 0.0
valid_count = 0
average = 0
while grade != -1:
    if grade < 0 and grade > 100:
        grade = float(input())
        continue

    valid_count += 1
    total_grade += grade
    grade = float(input())
average = total_grade / valid_count

print(valid_count)
print(f"{average:.2f}")
