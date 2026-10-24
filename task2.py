# Attendance Recovery Computation

total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
required_percentage = float(input("Enter required attendance percentage: "))

if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
    print("Invalid attendance details")
elif not 0 < required_percentage <= 100:
    print("Invalid eligibility percentage")
else:
    current_percentage = (attended_classes / total_classes) * 100

    print(f"\nCurrent Attendance: {current_percentage:.2f}%")
    print(f"Required Attendance: {required_percentage:.2f}%")

    if current_percentage >= required_percentage:
        print("Status: Eligible")

        print("Minimum consecutive classes required: 0")
    else:
        # Calculate classes needed if all future classes are attended
        classes_needed = 0

        while ((attended_classes + classes_needed) /
               (total_classes + classes_needed)) * 100 < required_percentage:
            classes_needed += 1

        print("Status: Not Eligible Yet")
        print("Minimum consecutive classes to attend:", classes_needed)

    # Future attendance scenarios
    future_classes = int(input("\nEnter number of future classes: "))

    if future_classes < 0:
        print("Invalid number of future classes")
    else:
        for attendance_rate in [1.0, 0.75, 0.50, 0.0]:
            future_attended = int(future_classes * attendance_rate)
            future_total = total_classes + future_classes
            future_percentage = (
                (attended_classes + future_attended) / future_total
            ) * 100

            print(
                f"Attending {attendance_rate * 100:.0f}% of future classes: "
                f"{future_percentage:.2f}%"
            )
