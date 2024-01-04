numeroTROCA = int(input())
numero = input().split()

print (numero)
lampA = 0
lampB = 0

for c in numero:
    if c == '1':
        lampA = 1 - lampA  # Alternar o estado da lâmpada A
    elif c == '2':
        lampA, lampB = 1 - lampA, 1 - lampB  # Alternar ambos os estados das lâmpadas

print(lampA)
print(lampB)
