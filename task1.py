
print("===== EXAMINATION RESULT SYSTEM =====")

num_subjects = int(input("Enter number of subjects: "))
pass_mark = float(input("Enter minimum pass mark: "))
max_marks = float(input("Enter maximum marks per subject: "))
grace_limit = float(input("Enter maximum grace marks per subject: "))

subjects = []
total_marks = 0
total_max_marks = 0
failed_subjects = 0
grace_used = 0

for i in range(num_subjects):
    print(f"\nSubject {i + 1}")
    name = input("Enter subject name: ")
    marks = float(input("Enter marks obtained: "))

    # Validate marks
    if marks < 0 or marks > max_marks:
        print("Invalid marks! Enter marks within the valid range.")
        continue

    final_marks = marks
    grace = 0

    # Apply grace marks only when needed to pass
    if marks < pass_mark:
        required_grace = pass_mark - marks

        if required_grace <= grace_limit:
            grace = required_grace
            final_marks = min(marks + grace, max_marks)
            print(f"Grace marks awarded: {grace}")
        else:
            print("Grace marks not sufficient to pass.")

    # Check final pass/fail status
    if final_marks >= pass_mark:
        status = "PASS"
    else:
        status = "FAIL"
        failed_subjects += 1

    total_marks += final_marks
    total_max_marks += max_marks
    grace_used += grace

    subjects.append((name, marks, grace, final_marks, status))

# Display subject-wise results
print("\n===== FINAL MARKSHEET =====")

for name, marks, grace, final_marks, status in subjects:
    print(f"\nSubject: {name}")
    print(f"Original Marks: {marks}")
    print(f"Grace Marks: {grace}")
    print(f"Final Marks: {final_marks}")
    print(f"Result: {status}")

# Calculate percentage
if total_max_marks > 0:
    percentage = (total_marks / total_max_marks) * 100
else:
    percentage = 0

print("\n===== OVERALL RESULT =====")
print(f"Total Marks: {total_marks}/{total_max_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Total Grace Marks Used: {grace_used}")

# Generate final classification
if failed_subjects > 0:
    classification = "FAIL"
elif percentage >= 75:
    classification = "DISTINCTION"
elif percentage >= 60:
    classification = "FIRST CLASS"
elif percentage >= 50:
    classification = "SECOND CLASS"
else:
    classification = "PASS"

print(f"Final Classification: {classification}")
