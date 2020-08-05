msg = input("What is your message? ")
shift = int(input("How many letters do you want to shift? "))
new_msg = ""
for l in msg:
    if l == " ": # replace space with space
        new_msg += " "
    elif ("a"<= l <= "z") and (ord(l) < 123-shift): # handle lowercase characters that don't wrap around
        new_msg += chr(ord(l)+shift)
    elif ("A"<= l <= "Z") and (ord(l) < 91-shift): # handle uppercase characters that don't wrap around
        new_msg += chr(ord(l)+shift)
    else: # handle characters that wrap around
        new_msg += chr(ord(l)+shift-26)

print(new_msg)
