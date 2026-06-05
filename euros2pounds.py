print("I will convert euros to pounds")

try:
    exchange_rate = float(input("Please enter the current exchange rate (1 euro = ? pounds): "))
    euro_amount = float(input("Please enter the amount of euros you want to convert: "))
    commission_rate = float(input("Please enter the commission rate (as a decimal, e.g., 0.05 for 5%): "))


    total_amount = euro_amount * exchange_rate
    total_amount_with_commission = total_amount * (1 - commission_rate)

    print(f"The total cost in pounds is: \u00A3{total_amount_with_commission:.2f} ")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit(1)