lista = [1, 2, 3]
listaModificada = [
    f"{item} é par" if item % 2 == 0 else f"{item} é impar" for item in lista
]
print(listaModificada)


