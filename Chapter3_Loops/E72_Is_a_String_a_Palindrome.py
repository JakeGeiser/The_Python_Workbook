word = input("Check if word is Palindrome: ")
w = word.lower()
l = len(word)

for i in range(0,l//2):
    if w[i] != w[l-1-i]:
        state = 0
        break
    else:
        state = 1

if state == 0:
    print(f"Sorry, {word} is not a palindrome.")

else:
    print(f"Yep, {word} is a palindrome.")
