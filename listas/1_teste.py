#A lista é um var que armazena outras variáveis.
L = [1, 3, 5, 7, 5.8, "Kaua"]
print(L)
#Adicionar var a lista
L.append(10)
print(L)
#Acessando elementos
#Se eu quiser acessar o elemento 1
print(L[0])
#Alterar valores
L[0] = 100
print(L[0])
print(L)
print(L[-1])
#Deletar elementos da lista
print(L)
del L[-1]
print(L)