# Ask user for the wavelength of light
wl = float(input("Wavelength of light you wish to inquire about in meters: "))

# gamma-ray
if wl <= 10**(-12):
    print(f"{wl}m is a gamma-ray")
# x-ray
elif 10**(-12) <= wl < 10**(-9):
    print(f"{wl}m is in x-ray range")
# ultraviolet
elif 10**(-9) <= wl < 400*10**(-9):
    print(f"{wl}m is in ultraviolet range")
# near-infrared
elif 750*10**(-9) <= wl < 2.5*10**(-6):
    print(f"{wl}m is in near-infrared range")
# infrared
elif 2.5*10**(-6) <= wl < 25*10**(-6):
    print(f"{wl}m is in infrared range")
# microwave
elif 25*10**(-6) <= wl < 10**(-3):
    print(f"{wl}m is in mircowave range")
# radio wave
elif 10**(-3) <= wl:
    print(f"{wl}m is in radio wave range")
# visible 750 to 380
else:
    print(f"{wl}m is in the visible range")