principal = float(input())
rate = float(input())
time = float(input())
interest = principal * rate / 100 * time
print(interest)
totalAmount = principal + principal * 1 * rate / 100 * time
print(totalAmount)
monthlyInterest = interest / time * 12
print(monthlyInterest)

