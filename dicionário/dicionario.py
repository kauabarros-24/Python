n = int(input())
dicio = {}
i = 0
while i < n:
    palavras = input().split()
    dicio[palavras[0]] = palavras[1]
    i+=1 

for valor in dicio.values():
    print(valor, end = " ")