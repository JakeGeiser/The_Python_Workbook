string = input("Check if phrase is Palindrome: ")
w = string.lower().replace(" ","")
l = len(w)

for i in range(0,l//2):
    if w[i] != w[l-1-i]:
        state = 0
        break
    else:
        state = 1

if state == 0:
    print(f"Sorry, \'{string}\' is not a palindrome.")

else:
    print(f"Yep, \'{string}\' is a palindrome.")
