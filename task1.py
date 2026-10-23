
# Campus Event Financial Planning

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input event expenses
venue_cost = float(input("Enter venue cost: ₹"))
equipment_cost = float(input("Enter equipment cost: ₹"))
catering_cost = float(input("Enter catering cost: ₹"))
transport_cost = float(input("Enter transport cost: ₹"))
certificate_cost = float(input("Enter certificate cost per participant: ₹"))

# Input participant and funding details
expected_participants = int(input("Enter expected participants: "))
registration_fee = float(input("Enter registration fee per participant: ₹"))
sponsorship = float(input("Enter sponsorship amount: ₹"))

# Calculate fixed expenses
fixed_cost = (
    venue_cost + equipment_cost + transport_cost
)

# Calculate total event expenses
catering_total = catering_cost * expected_participants
certificates_total = certificate_cost * expected_participants

total_cost = fixed_cost + catering_total + certificates_total

# Calculate participant contributions
participant_contributions = (
    expected_participants * registration_fee
)

# Calculate total available funds
total_funds = participant_contributions + sponsorship

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - total_funds)

# Calculate break-even registrations
variable_cost_per_person = catering_cost + certificate_cost
contribution_per_person = registration_fee - variable_cost_per_person

if contribution_per_person > 0:
    remaining_fixed_cost = max(0, fixed_cost - sponsorship)
    break_even_count = (
        int(remaining_fixed_cost // contribution_per_person)
        + (1 if remaining_fixed_cost % contribution_per_person > 0 else 0)
    )
else:
    break_even_count = None

# Display financial report
print("\n===== EVENT FINANCIAL REPORT =====")
print(f"Venue Cost: ₹{venue_cost:.2f}")
print(f"Equipment Cost: ₹{equipment_cost:.2f}")
print(f"Catering Cost: ₹{catering_total:.2f}")
print(f"Transport Cost: ₹{transport_cost:.2f}")
print(f"Certificate Cost: ₹{certificates_total:.2f}")
print(f"Total Event Cost: ₹{total_cost:.2f}")

print(f"Participant Contributions: ₹{participant_contributions:.2f}")
print(f"Sponsorship Received: ₹{sponsorship:.2f}")
print(f"Total Available Funds: ₹{total_funds:.2f}")
print(f"Sponsorship/Funding Shortfall: ₹{shortfall:.2f}")

if break_even_count is not None:
    print(f"Minimum Break-Even Registrations: {break_even_count}")

    if break_even_count <= expected_participants:
        print("Status: Break-even is achievable.")
    else:
        print("Status: More registrations or additional funding are needed.")
else:
    print("Break-even is not achievable at the current registration fee.")
    print("Increase the fee or reduce variable costs.")
