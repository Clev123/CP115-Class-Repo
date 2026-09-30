target_points = int(input())
total_points = 0
rounds_played = 0
while total_points < target_points:
    points = int(input())
    rounds_played += 1
    total_points += points
print(total_points)
print(rounds_played)
