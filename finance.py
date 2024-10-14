# finance-calc-formulas
#Created a calculator for both simple and compound interest.
def calc_compound_interest(principal, rate, years):
    """Calculate the total cost using compound interest."""
    total_cost = principal * (1 + rate / 100) ** years
    return total_cost

def calc_simple_interest(principal, rate, years):
    """Calculate the total cost using simple interest."""
    total_cost = principal * (1 + (rate / 100) * years)
    return total_cost

def calc_monthly_payment(principal, rate, months):
    """Calculate the monthly payment necessary to pay off the principal."""
    monthly_rate = rate / 100 / 12
    if monthly_rate == 0:
        return principal / months  # No interest case
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    return monthly_payment

def main():
    # Get user input
    car_model = input("What kind of car would you like to buy? ")
    cost = float(input("How much does it cost? "))
    interest_rate = float(input("What is the interest rate? [e.g., 2.5] "))
    months = int(input("How many months? [e.g., 36 or 48 or 72] "))

    # Calculate total cost and monthly payment
    total_cost = calc_compound_interest(cost, interest_rate, months / 12)
    monthly_payment = calc_monthly_payment(cost, interest_rate, months)

    # Print results
    print(f"The total cost of the {car_model} is ${total_cost:.2f}.")
    print(f"Your monthly payment will be ${monthly_payment:.2f}.")

main()

