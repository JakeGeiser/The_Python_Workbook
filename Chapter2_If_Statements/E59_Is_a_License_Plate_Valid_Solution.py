plate = input("Enter the license plate(leave out special characters.): ")

if (len(plate) == 6 and 
    "AAA" <= plate[0:3] <= "ZZZ" and
    "000" <= plate[3:7] <= "999"):
    print(f"The plate: {plate}, is a valid older style plate.")
    
elif (len(plate) == 7 and 
    "AAA" <= plate[0:3] <= "ZZZ" and
    "0000" <= plate[3:8] <= "9999"):
    print(f"The plate: {plate}, is a valid newer style plate.")

else:
    print(f"The plate: {plate}, is not a valid plate.")