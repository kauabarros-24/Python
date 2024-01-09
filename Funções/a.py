def calculo(x, y):
    resp = x * x + y * y
    return resp, x, y

resultado = calculo(10, 2)
print(resultado)
arroz, x, *_ =  calculo(10, 2)
print(arroz)
print(x)
#[Listas], (Tuplas) = Não podem ser modificadas, {dicty}