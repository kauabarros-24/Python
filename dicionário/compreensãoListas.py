lista_de_inteiros = map(int, input().split())

resultado = [valor *  2 if valor % 2 == 0 else valor * 3 for valor in lista_de_inteiros]

print(resultado)
