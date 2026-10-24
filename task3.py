# ATM Transaction Sequence Simulation

balance = float(input("Enter initial balance: "))
withdrawal_limit = 10000

total_deposits = 0
total_withdrawals = 0
successful_transactions = 0
rejected_transactions = 0

n = int(input("Enter number of transactions: "))

if balance < 0 or n < 0:
    print("Invalid input")
else:
    for i in range(n):
        print("\nTransaction", i + 1)
        transaction = input("Enter deposit or withdraw: ").lower()
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Rejected: Invalid amount")
            rejected_transactions += 1

        elif transaction == "deposit":
            balance += amount
            total_deposits += amount
            successful_transactions += 1
            print("Deposit successful")

        elif transaction == "withdraw":
            if amount > withdrawal_limit:
                print("Rejected: Withdrawal limit exceeded")
                rejected_transactions += 1

            elif amount > balance:
                print("Rejected: Insufficient balance")
                rejected_transactions += 1

            else:
                balance -= amount
                total_withdrawals += amount
                successful_transactions += 1
                print("Withdrawal successful")

        else:
            print("Rejected: Invalid transaction type")
            rejected_transactions += 1

    print("\n===== ATM TRANSACTION SUMMARY =====")
    print(f"Final Balance: Rs. {balance:.2f}")
    print(f"Total Deposits: Rs. {total_deposits:.2f}")
    print(f"Total Withdrawals: Rs. {total_withdrawals:.2f}")
    print("Successful Transactions:", successful_transactions)
    print("Rejected Transactions:", rejected_transactions)