risada = input()
gambeta = ""

for r in risada.lower():
    if (r == "a" or r == "e" or r == "i" or r == "o" or r == "u"):
        gambeta += r


if (gambeta == gambeta[::-1]):
    print("S")
else:
    print("N")