# Pure math/logic function
def compute_pay(hours, rate):
    if hours <= 0 or rate <= 0:
        raise ValueError("Hours and rate must be positive")

    reg_hours = min(hours, 40)
    ot_hours = max(0, hours - 40)
    return (reg_hours * rate) + (ot_hours * rate * 1.5)


if __name__ == "__main__":
    # Interactive I/O happens outside
    try:
        user_hours = float(input("Enter hours worked: "))
        user_rate = float(input("Enter hourly rate: "))
    
        pay = compute_pay(user_hours, user_rate)
        print(f"Total pay: {pay:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
