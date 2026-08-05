item_name = input(" Enter item name: ")
price = float(input(" Enter item price: "))
quantity = 3
tax_rate = 0.06
subtotal = 3 * price
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
print(f" Subtotal: {subtotal}")
print(f" Tax: {tax_amount}")
print(f" Total: {total}")