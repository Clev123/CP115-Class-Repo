position = input()
overtime_hours = int(input())
is_weekend = input()
if position == "Manager":
    hourly_rate = 30
elif position == "Supervisor":
    hourly_rate = 20 
elif position == "Staff":
    hourly_rate = 15
else:
    hourly_rate = 8
if overtime_hours <= 8:
    overtime = 1.5 * hourly_rate * overtime_hours
else:
    overtime = (8 * hourly_rate *1.5) + ((overtime_hours - 8) * hourly_rate * 2)
if is_weekend == "yes":
    overtime_pay = overtime + 5 * overtime_hours
else:
    overtime_pay = overtime
print(overtime_pay)
