def medianof(a,b,c):
    if b<= a <= c or c <= a <=b:
        print(f"{a} is the median")
    elif a<= b <= c or c <= b <=a:
        print(f"{b} is the median")
    elif b<= c <= a or a <= c <=b:
        print(f"{c} is the median")

medianof(7,7,5)