Dias = int(input())
soma = 0
i = 0

while i < Dias:
    soma += int(input())
    i+=1
    if (soma >= 1000000):
        break

print(i)
    