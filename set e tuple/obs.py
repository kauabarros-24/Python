#O set é segue a ideia de conjunto

#set_exemplo = {1, 2, 3}
#Note que, diferentes dos dicionários, o set usa vírgula e não tem chave, como nos dicionários
#print(type(set_exemplo))
#print(set_exemplo)

#Há como criar um set vazio
#setVazio = set()
#print(setVazio)
#print(type(setVazio))

#Podemos passar a lista para o set, pois não há elementos duplicados no set
#lista = [1, 2, 3, 4, 4, 5, 5, 5]
#setLista = set(lista)
#print(lista, setLista)
#Podemos remover o set de volta para a lista
#listaSet = list(setLista)
#print(listaSet)

#Podemos adicionar elementos no set:
#setAdd = {1, 2}
#print(setAdd)
#setAdd.add(3)
#print(setAdd)
#Podemos remover:
#setAdd.remove(3)
#print(setAdd)
#Podemos descartar  elementos inexistentes:

#setAdd.discard(2)
#print(setAdd)
#setAdd.add(2)
#print(setAdd)
#setAdd.remove(2)
#print(setAdd)
#print(setAdd)

#setEx = {1, 5, 3, 7}
#for i in setEx:
    #print(i)

#Verificar existência de um elemento:

#set_exemplo = {1, 2, 3}
#print(1 in set_exemplo)
#print(4 in set_exemplo)

#Unir sets:
#set1 = {1, 2}
#set2 = {2, 3}
#Note que, como o set não duplica elementos, só restará um "2":
#print(set1 | set2)
#print(set1.union(set2))

#Interseção: -> Note que só saíra 2
#print(set1 & set2)
#print(set1.intersection(set2))

#Diferença
#print(set1 - set2)
#print(set1.difference(set2))