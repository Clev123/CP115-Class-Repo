sales = int(input())
prev_sales = 0
count = 0
record_days = 0 
while sales != 0:
    count += 1
    if sales > prev_sales:
        record_days += 1
    prev_sales = sales
    sales = int(input())
print(count)
print(record_days)
