hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

overtime = hours - 40 if hours > 40 else 0

if hours > 40:
    overtime_pay = overtime * rate * 1.5
else:
    overtime_pay = 0

if hours < 0 or rate < 0:
    print("Invalid input. Hours and rate must be non-negative.")
    exit(1)

total_pay = (hours - overtime) * rate + overtime_pay

print(f"Total pay: £{total_pay:.2f}")