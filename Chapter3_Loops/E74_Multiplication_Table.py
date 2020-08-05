MIN = 1
MAX = 10

size = len(str(MAX*MAX)) + 2

print("{0:<{1}}".format(""[:size],size), end="")

for width in range(MIN,MAX+1):
    print("{0:<{1}}".format(str(width)[:size],size), end="")
print(" ")

for length in range(1,MAX+1):
    print("{0:<{1}}".format(str(length)[:size],size), end="")
    for width in range(1,MAX+1):
        print("{0:<{1}}".format(str(width*length)[:size],size), end="")
    print("")