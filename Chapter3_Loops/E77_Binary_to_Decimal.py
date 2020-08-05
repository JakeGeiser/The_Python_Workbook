# Get binary number from user
binary = input("Enter binary number: ")

# store length of given binary number
l = len(binary)

# Start base-10 number value
val = 0

# Add appropriate base-10 values for each 0/1 in binary string
for i in range(0,l):
    val += int(binary[l-1-i]) * 2**i

print(f"{binary} is equivalent to {val} in base 10!")