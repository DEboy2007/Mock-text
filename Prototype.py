from random import randint

original = input("Enter sentence: ")
final = ""
for i in original:
    if randint(1, 2) == 1:
        final += i.upper()
    else:
        final += i.lower()
print(final)
