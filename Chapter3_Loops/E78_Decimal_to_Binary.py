# Get decimal number from user
q = int(input("Enter decimal(base-10) number: "))
# convert string to integer
val = str()

# convert to binary
while q != 0:
    # Get remainder of division by 2
    v = q%2 
    # Add the remainder (0 or 1) to the front of our value string
    val = str(v) + val
    # Change q to the integer division of q and 2
    q = q//2

print(val)
