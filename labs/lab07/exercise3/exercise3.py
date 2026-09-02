name = input()
price = float(input())
quantity = int(input())
member_answer = input()

order_total = price * quantity
if order_total >= 100:
    free_shipping = "True"
else:
    free_shipping = "False"
    
if member_answer == "yes":
    is_member = True
else:
    is_member = False

print(name.upper())
print(order_total)
print(free_shipping)
print(is_member)
