drink_price = float(input())
drink_qty = int(input())
cake_price = float(input())
cake_qty = int(input())

subtotal = drink_price * drink_qty + cake_price * cake_qty
service_charge = subtotal * 0.1
final = subtotal + service_charge - 2

print(subtotal)
print(service_charge)
print(final)
