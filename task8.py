
# Repeated Transaction Detection

transactions = [
    ("T101", 500),
    ("T102", 1200),
    ("T103", 800),
    ("T101", 500),
    ("T104", 6000),
    ("T105", 1500),
    ("T102", 1200)
]

threshold = 5000

seen = set()
suspicious = []

print("Transaction Report")
print("-" * 40)

for transaction_id, amount in transactions:
    reasons = []

    # Check for duplicate transaction IDs
    if transaction_id in seen:
        reasons.append("Duplicate Transaction")
    else:
        seen.add(transaction_id)

    # Check amount threshold
    if amount > threshold:
        reasons.append("Threshold Violation")

    # Store suspicious transactions
    if reasons:
        suspicious.append(
            (transaction_id, amount, reasons)
        )

# Display suspicious transactions
print("\nSuspicious Transactions:")

if suspicious:
    for tid, amount, reasons in suspicious:
        print("Transaction ID:", tid)
        print("Amount: Rs.", amount)
        print("Reason:", ", ".join(reasons))
        print("-" * 40)
else:
    print("No suspicious transactions found.")

print("Total Transactions:", len(transactions))
print("Suspicious Entries:", len(suspicious))
