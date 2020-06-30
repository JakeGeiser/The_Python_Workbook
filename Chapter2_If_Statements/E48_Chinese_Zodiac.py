# Ask user to input birth year
born = int(input("Please input the year your were born. \n"))

# Determine what integer year they were born for assigning zodiac
Off_2000 = born - 2000
rem = Off_2000 % 12

# print zodiac based of remander integer
if rem == 0:
    print("You were born the year of the Dragon!")
elif rem == 1:
    print("You were born the year of the Snake!")
elif rem == 2:
    print("You were born the year of the Horse!")
elif rem == 3:
    print("You were born the year of the Sheep!")
elif rem == 4:
    print("You were born the year of the Monkey!")
elif rem == 5:
    print("You were born the year of the Rooster!")
elif rem == 6:
    print("You were born the year of the Dog!")
elif rem == 7:
    print("You were born the year of the Pig!")
elif rem == 8:
    print("You were born the year of the Rat!")
elif rem == 9:
    print("You were born the year of the Ox!")
elif rem == 10:
    print("You were born the year of the Tiger!")
else:
    print("You were born the year of the Hare!")