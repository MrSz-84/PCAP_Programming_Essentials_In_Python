income = float(input("Input your annual income value: "))

# tax calculator
if income <= 85258:
    tax = income * 0.18 - 556.2
    if tax <= 0:
        tax = 0
elif income > 85258:
    tax = 14839.2 + (income - 85528) * 0.32
    if tax <= 0:
        tax = 0
# result
tax = round(tax, 0)
print("Your tax is equal to: ", tax, "talarów")