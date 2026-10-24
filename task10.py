
# Warehouse Inventory Reconciliation

products = int(input("Enter number of products: "))

for i in range(products):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    closing = int(input("Enter actual closing stock: "))
    minimum = int(input("Enter minimum required stock: "))

    # Calculate expected closing stock
    expected = opening + incoming - dispatched

    # Calculate discrepancy
    discrepancy = closing - expected

    # Calculate replenishment requirement
    replenishment = max(0, minimum - closing)

    print("\n--- Inventory Report ---")
    print("Product Name:", name)
    print("Expected Closing Stock:", expected)
    print("Actual Closing Stock:", closing)

    if discrepancy == 0:
        print("Status: No Discrepancy")
    else:
        print("Status: Discrepancy Detected")
        print("Discrepancy Quantity:", discrepancy)

    if replenishment > 0:
        print("Replenishment Required:", replenishment)
    else:
        print("Stock Level: Sufficient")

    print("------------------------")
