# Store tax and tip rates
tipp = 0.18 # 18 percent tip
taxp = 0.0675 # 6.75 percent tax (NC)

# Ask for cost of meal
raw = float(input("What is the menu cost of your meal? \n"))

# Calcualte tip
tip = raw * tipp
# Calcualte tax
tax = raw * taxp

# Print the tax, tip, and total amounts
print(f"You should tip ${tip:.2f}")
print(f"Your tax come out as ${tax:.2f}")
print(f"Your total comes out as ${(raw+tax+tip):.2f}")
