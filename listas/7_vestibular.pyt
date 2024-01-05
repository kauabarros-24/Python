numerosDeQuestoes = input()
gabaritoOficial = input()
seuGabarito = input()
lista = []
listaOficial = []
i = 0
contadorAcertos = 0

for acertos in seuGabarito:
    lista.append(acertos)

for resp in gabaritoOficial:
    listaOficial.append(resp)

while i < int(numerosDeQuestoes):
    if (lista[i] == listaOficial[i]):
        contadorAcertos+=1
    i+=1

print(contadorAcertos)









