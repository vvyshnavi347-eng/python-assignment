# Warehouse Inventory Reconciliation

n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products")
else:
    total_discrepancies = 0
    total_replenishment = 0

    for i in range(n):
        print(f"\nProduct {i + 1}")

        name = input("Enter product name: ")
        opening = int(input("Enter opening stock: "))
        incoming = int(input("Enter incoming quantity: "))
        dispatched = int(input("Enter dispatched quantity: "))
        actual_closing = int(input("Enter actual closing stock: "))
        minimum_stock = int(input("Enter minimum required stock: "))

        if min(opening, incoming, dispatched, actual_closing,
               minimum_stock) < 0:
            print("Invalid stock values")
            continue

        if dispatched > opening + incoming:
            print("Warning: Dispatch exceeds available stock")
            total_discrepancies += 1
            continue

        expected_closing = opening + incoming - dispatched
        discrepancy = actual_closing - expected_closing

        replenishment = max(0, minimum_stock - actual_closing)

        print("\nProduct:", name)
        print("Expected Closing Stock:", expected_closing)
        print("Actual Closing Stock:", actual_closing)

        if discrepancy == 0:
            print("Status: Stock Matched")
        else:
            print("Discrepancy:", discrepancy)
            if discrepancy < 0:
                print("Status: Stock Shortage")
            else:
                print("Status: Excess Stock")
            total_discrepancies += 1

        print("Replenishment Required:", replenishment)

        total_replenishment += replenishment

    print("\n===== INVENTORY SUMMARY =====")
    print("Products with Discrepancies:", total_discrepancies)
    print("Total Replenishment Required:", total_replenishment)