line = input("Enter 8 bits: ")

while line != "":
    # Check line if it has 8 characters
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        print("What you entered is not 8 bits, please try again(1s and 0s only).")
    else:
        # counet ones
        ones = line.count("1")

        if ones % 2 == 0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit shoule be 1.")
            
    line = input("Enter 8 bits: ")
