#List of original prices
org = [4.95,9.95,14.95,19.95,24.95]
discount = 0.60
print("Orginal  Discount  New")
for p in org:
    dis = p * discount
    new = p - dis
    print(f"{p:.2f}      {dis:.2f}     {new:.2f}")