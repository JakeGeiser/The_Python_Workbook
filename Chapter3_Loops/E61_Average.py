# Create while loop that will average all inputs
print("Enter STOP when you want to stop adding numbers.")
count = 0
num = 0
while True:
    x = input("What number would you like to include in average? ")
    if x == "STOP":
        break
    else:
        count += 1
        num += float(x)

print(f"The average is {num/count}")
