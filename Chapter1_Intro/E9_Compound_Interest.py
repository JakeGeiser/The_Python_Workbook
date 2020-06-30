# Ask user for initial bank balance
x = float(input("What is your initial deposit/balance? \n"))

r = 1.04 # 4% compunt interest yearly

x = x * r
print(f"Your balance after 1 year is ${x:.2f}")

x = x * r
print(f"Your balance after 2 years is ${x:.2f}")

x = x * r
print(f"Your balance after 3 years is ${x:.2f}")