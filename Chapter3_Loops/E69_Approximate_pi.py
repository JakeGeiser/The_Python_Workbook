# ask for number ov terms
n = int(input("How many terms from the seires would you like to compute? "))

for i in range(1,n+1):
    if i == 1:
        pi = 3.
        print(f"pi = {pi}")
    else:
        t = 2*(i-1)
        pi += (-1)**(i) * 4./(t*(t+1)*(t+2))
        print(f"pi = {pi}")