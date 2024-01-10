n = int(input())
i = 0
lista = []
tupla = ()
while i < n:
    a = input().split()
    tupla = tuple(a)
    lista.append(tupla)
    i+=1

print(lista)
