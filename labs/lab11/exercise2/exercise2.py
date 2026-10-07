score = int(input())
turn = 1
total_a = 0
total_b = 0
winner = 0
while score != -1:
    if turn % 2 == 0:
        total_b += score
    else:
        total_a += score
    if total_a > total_b:
        winner = "A"
    elif total_a < total_b:
        winner = "B"
    else:
        winner = "Tie"
    turn += 1
    score = int(input())
print(total_a)
print(total_b)
print(winner)
