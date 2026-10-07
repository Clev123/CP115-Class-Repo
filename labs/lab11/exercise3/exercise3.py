number = int(input())
prev_number = 0
count = 0 
biggest_jump = 0
while number != 0:
    count += 1
    if prev_number != 0:
        jump = number - prev_number
        if jump > biggest_jump:
            biggest_jump = jump
    prev_number = number
    number = int(input())

print(count)
print(biggest_jump)
