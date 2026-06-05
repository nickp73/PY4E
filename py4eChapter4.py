
def compute_pay():
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    if hours <= 0 or rate <= 0:
        raise ValueError("Hours and rate must be positive")

    overtime_rate = 1.5 * rate

    if hours <= 40:
        return hours * rate
    else:
        return 40 * rate + (hours - 40) * overtime_rate


print(f"Total pay: {float(compute_pay()):.2f}")

