# Ask user for licenseplate
lp = input("What is the licenseplat?(Only include numbers and letters.) \n")

# Check if the string is allowed
if lp.isalnum() == False:
    print("Please ensure input only has numbers and letters.")

# Check 7 length license plates
elif len(lp) == 7:
    first = str()
    second = str()
    count = 0
    for letter in lp:
        if count <3:
            first += letter
        else:
            second += letter
        count += 1
    if first.isalpha() == True:
        if second.isnumeric() == True:
            print(f"{lp} is a new valid license plate")
        else:
            print(f"{lp} is not a valid license plate.")
    else:
        print(f"{lp} is not a valid license plate.")

# Check 6 length license plates
elif len(lp) == 6:
    first = str()
    second = str()
    count = 0
    for letter in lp:
        if count <3:
            first += letter
        else:
            second += letter
        count += 1
    if first.isalpha() == True:
        if second.isnumeric() == True:
            print(f"{lp} is an old valid license plate")
        else:
            print(f"{lp} is not a valid license plate.")
    else:
        print(f"{lp} is not a valid license plate.")

else:
    print(f"{lp} is not a valid license plate.")