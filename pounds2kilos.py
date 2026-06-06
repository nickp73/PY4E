print("I will convert a weight from pounds to kilograms")

try:
    weight_in_lbs = float(input("Please enter your weight in pounds: "))
except ValueError:
    print("Invalid input. Please enter a numeric weight in pounds.")
    exit(1)

try:
    decimal_places = int(input("Please enter the number of decimal places you want to round to: "))
    if decimal_places < 0:
        raise ValueError("Decimal places cannot be negative.")
except ValueError as e:
    print(f"Invalid input. {e}. Please enter a non-negative integer for decimal places.")
    exit(1)

converted_weight = weight_in_lbs * 0.45359237
rounded_weight = round(converted_weight, decimal_places)

print(f"Your weight in kilograms is: {rounded_weight} kg")