def calculate_total(price, tax):

    if price < 0 or tax < 0:
        raise ValueError("Price and tax cannot be negative")

    tax_amount = price * tax / 100

    total = price + tax_amount

    return total


# Main program
price = 1000
tax = 18

result = calculate_total(price, tax)

print("Original Price:", price)
print("Tax Percentage:", tax, "%")
print("Final Amount:", result)
