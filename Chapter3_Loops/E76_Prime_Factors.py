n = 0
while n < 2:
    n = int(input("Enter interger (2 or larger): "))

f = 2

print("Prime factors are as follows:")

while f <= n:
    if n % f == 0:
         print("%3d" % f, end="")
         n = n//f
    else:
        f += 1
