
# Smart Public Transport Fare Reconciliation

# Fare details for each route
route_fares = {
    "Route A": 20,
    "Route B": 30,
    "Route C": 40
}

# Passenger category discounts
discounts = {
    "Adult": 0.0,
    "Student": 0.5,
    "Senior": 0.3
}

expected_revenue = 0
collected_revenue = 0

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\nTransaction", i + 1)

    route = input("Enter route (Route A, Route B, Route C): ")
    category = input("Enter category (Adult, Student, Senior): ")
    passengers = int(input("Enter number of passengers: "))
    collected = float(input("Enter collected amount: "))

    if route not in route_fares or category not in discounts:
        print("Invalid route or passenger category!")
        continue

    if passengers <= 0 or collected < 0:
        print("Invalid passenger count or amount!")
        continue

    base_fare = route_fares[route]
    discount = discounts[category]

    fare_per_person = base_fare * (1 - discount)
    expected = fare_per_person * passengers

    expected_revenue += expected
    collected_revenue += collected

    difference = collected - expected

    print("Expected Fare:", round(expected, 2))
    print("Collected Fare:", round(collected, 2))

    if difference < 0:
        print("Discrepancy: Undercollection of", round(-difference, 2))
    elif difference > 0:
        print("Discrepancy: Overcollection of", round(difference, 2))
    else:
        print("No discrepancy")

print("\n--- FINAL RECONCILIATION REPORT ---")
print("Total Expected Revenue:", round(expected_revenue, 2))
print("Total Collected Revenue:", round(collected_revenue, 2))

difference = collected_revenue - expected_revenue

if difference < 0:
    print("Total Undercollection:", round(-difference, 2))
elif difference > 0:
    print("Total Overcollection:", round(difference, 2))
else:
    print("Revenue Fully Reconciled")

print("Reconciliation Completed.")
