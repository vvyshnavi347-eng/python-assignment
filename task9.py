
# Campus Event Financial Planning

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input fixed expenses
venue = float(input("Enter venue cost: ₹"))
equipment = float(input("Enter equipment cost: ₹"))
transport = float(input("Enter transport cost: ₹"))

# Input variable expenses
catering_per_person = float(input("Enter catering cost per person: ₹"))
certificate_per_person = float(input("Enter certificate cost per person: ₹"))

# Input event details
participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant: ₹"))
sponsorship = float(input("Enter sponsorship amount: ₹"))

# Calculate expenses
fixed_cost = venue + equipment + transport
variable_cost_per_person = (
    catering_per_person + certificate_per_person
)

total_variable_cost = variable_cost_per_person * participants
total_cost = fixed_cost + total_variable_cost

# Calculate revenue
registration_income = registration_fee * participants
total_income = registration_income + sponsorship

# Calculate sponsorship shortfall
sponsorship_needed = max(0, total_cost - registration_income)
sponsorship_shortfall = max(0, sponsorship_needed - sponsorship)

# Calculate break-even registrations
contribution_per_person = (
    registration_fee - variable_cost_per_person
)

if contribution_per_person > 0:
    minimum_registrations = max(
        0,
        int(fixed_cost - sponsorship)
        // int(contribution_per_person)
    )
    # Correctly round up the break-even requirement
    import math
    minimum_registrations = max(
        0,
        math.ceil((fixed_cost - sponsorship)
                  / contribution_per_person)
    )
elif fixed_cost <= sponsorship:
    minimum_registrations = 0
else:
    minimum_registrations = None

# Display financial report
print("\n===== EVENT FINANCIAL REPORT =====")
print(f"Fixed expenses: ₹{fixed_cost:.2f}")
print(f"Variable expenses: ₹{total_variable_cost:.2f}")
print(f"Total event cost: ₹{total_cost:.2f}")
print(f"Registration income: ₹{registration_income:.2f}")
print(f"Sponsorship received: ₹{sponsorship:.2f}")
print(f"Total income: ₹{total_income:.2f}")
print(f"Sponsorship shortfall: ₹{sponsorship_shortfall:.2f}")

if minimum_registrations is not None:
    print("Minimum registrations to break even:",
          minimum_registrations)
else:
    print("Break-even is impossible at the current fee.")

if total_income >= total_cost:
    print("Event Status: Budget Balanced")
else:
    print(f"Event Deficit: ₹{total_cost - total_income:.2f}")
