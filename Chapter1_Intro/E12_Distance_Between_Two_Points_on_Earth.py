#import numpy as np
import numpy as np
# Ask latitude and longitude of first location
t1 = np.radians(float(input("What is the latitude of first location? \n")))
g1 = np.radians(float(input("What is the longitude of first location? \n")))
# Ask latitude and longitude of second location
t2 = np.radians(float(input("What is the latitude of second location? \n")))
g2 = np.radians(float(input("What is the longitude of second location? \n")))

dist = 6371.01 * np.arccos(np.sin(t1)*np.sin(t2)+np.cos(t1)*np.cos(t2)*np.cos(g1-g2))
print(f"The distance between the two points is {dist}km")