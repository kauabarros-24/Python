lista = [1, 2, 3, 4, 5]

#dicio = {}

#dicio = {item: item * item for item in lista}
#dicio = {item: item for item in lista if item % 2 == 0}
#print(dicio)
alunos = {
    "tiago": 10,
    "osvaldo": 8,
    "Mathias": 6
}
dicio = {
    chave.upper(): valor + 1 if valor <= 9 else valor for chave, valor in alunos.items()
}
print(dicio)
