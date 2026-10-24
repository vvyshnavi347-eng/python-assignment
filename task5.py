from datetime import datetime, timedelta
import math

# Smart Parking Fee Management

rates = {
    "bike": 20,
    "car": 50,
    "truck": 80
}

daily_limits = {
    "bike": 200,
    "car": 500,
    "truck": 800
}

total_vehicles = int(input("Enter number of vehicles: "))

if total_vehicles <= 0:
    print("Invalid number of vehicles")
else:
    total_revenue = 0

    for i in range(total_vehicles):
        print(f"\nVehicle {i + 1}")

        vehicle = input(
            "Enter vehicle type (bike/car/truck): "
        ).lower()

        if vehicle not in rates:
            print("Invalid vehicle category")
            continue

        entry = input("Enter entry time (HH:MM): ")
        exit_time = input("Enter exit time (HH:MM): ")

        try:
            entry_dt = datetime.strptime(entry, "%H:%M")
            exit_dt = datetime.strptime(exit_time, "%H:%M")

            if entry_dt.strftime("%H:%M") != entry:
                raise ValueError

            if exit_dt.strftime("%H:%M") != exit_time:
                raise ValueError

        except ValueError:
            print("Invalid time format. Use HH:MM.")
            continue

        # Calculate duration, allowing overnight parking
        if exit_dt < entry_dt:
            exit_dt += timedelta(days=1)

        duration = (exit_dt - entry_dt).total_seconds() / 3600

        if duration == 0:
            print("Invalid parking duration")
            continue

        # Charge each started hour
        hours = math.ceil(duration)

        # Daily charge with daily maximum
        days = math.ceil(duration / 24)
        fee = min(
            hours * rates[vehicle],
            days * daily_limits[vehicle]
        )

        # Penalty for parking longer than 48 hours
        penalty = 0

        if duration > 48:
            penalty = 200

        total_fee = fee + penalty
        total_revenue += total_fee

        print("\n----- PARKING BILL -----")
        print("Vehicle Type:", vehicle.capitalize())
        print(f"Parking Duration: {duration:.2f} hours")
        print("Charged Hours:", hours)
        print(f"Base Fee: Rs. {fee:.2f}")
        print(f"Penalty: Rs. {penalty:.2f}")
        print(f"Total Fee: Rs. {total_fee:.2f}")

    print("\n===== DAILY PARKING SUMMARY =====")
    print(f"Total Revenue: Rs. {total_revenue:.2f}")