x = float(input('What would you like the square root of? '))

g = x/2.
c = 0
while (g**2 - x) >= 10^(-12):
    c += 1
    g = (g+x/g)/2.
    if c >= 10000:
        break

print(f"The squre root of {x} is approximately {g}")