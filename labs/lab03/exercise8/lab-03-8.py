principal = float(input())
rate = float(input())
time = float(input())
interest = principal * rate * time
print(interest)
totalAmount = principal + principal * 1 * rate * time
print(totalAmount)
monthlyInterest = interest / time * 12
print(monthlyInterest)
