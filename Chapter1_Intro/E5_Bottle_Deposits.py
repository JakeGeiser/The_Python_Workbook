# Ask how many containers of 1 liter or less
small = float(input("How many drink containers that hold one liter or less would you like to turn in? "))
# Report refund value of small
sval = small*0.10
print(f"Your small containers get you ${sval:.2f}")

# Ask how many containers more than 1 liter
large = float(input("How many drink containers that hold more than one liter would you like to turn in? "))
# Report refund value of large
lval = round(large*0.25,2)
print(f"Your large containers get you ${lval:.2f}")

# Report total refund
print(f"Your total refund is ${(sval+lval):.2f}")