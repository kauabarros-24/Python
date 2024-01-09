numerosSeq = int(input())
n = input().split()

lista = []
for i in n:
    i = int(i)
    lista.append(i)

lista.sort()

for n in lista:
    print(n, end=" ")
