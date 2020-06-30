### Print out a table of Celcius and Fahrenheit

# Celcius to Fahrenheit conversion function
def fahren(x):
    return ((x * 9./5.) + 32)

# Print the conversion table
print("Celcius   Fahrenheit")
for i in range(0,101,10):
    print(f"  {i}        {fahren(i)}              {fahren(i+10)-fahren(i)}")