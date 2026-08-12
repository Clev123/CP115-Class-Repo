# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
# Creating a formatted table
coffee_name = "Coffee"
coffee_price = 3.50
coffee_quantity = 2

muffin_name = "Muffin"
muffin_price = 2.10
muffin_quantity = 3

water_name = "Water"
water_price = 1.05
water_quantity = 4

coffee_total = coffee_price * coffee_quantity
muffin_total = muffin_price * muffin_quantity
water_total = water_price * water_quantity

subtotal = coffee_total + muffin_total + water_total
tax = subtotal * 0.06
final_total = subtotal + tax

print( f"========== RECEIPT ==========\n"
       f"Item\tPrice\tQty\tTotal\n"
       f"\n{coffee_name}\t${coffee_price:.2f}\t{coffee_quantity}\t${coffee_total:.2f}"
       f"\n{muffin_name}\t${muffin_price:.2f}\t{muffin_quantity}\t${muffin_total:.2f}"
       f"\n{water_name}\t${water_price:.2f}\t{water_quantity}\t${water_total:.2f}"
       f"\n------------------------------"
       f"\nSubtotal\t\t${subtotal:.2f}"
       f"\nTax\t\t\t${tax:.2f}"
       f"\nTotal\t\t\t${final_total:.2f}"
       f"\n==============================")