total = 0
while True:
    x = input("Cost of individual item? (Enter nothing when done). ")
    if x == "":
        break

    total += round(float(x)*100.)

print(f"Total cost if paying with card is ${(float(total)/100.):.2f}")
if ((total % 5) < 2.5):
    total = total - (total%5)
    print(f"Total cost if paying with cash is ${(float(total)/100.):.2f}")

else:
    total = total + (5 - (total%5))
    print(f"Total cost if paying with cash is ${(float(total)/100.):.2f}")