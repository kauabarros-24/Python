#dicionario = {} #Criando um dicionário
#print(type(dicionario))

dicionario = {
    "Kaua": "martinsbarroskaua@gmail.com",
    "Pedrinho": "pedrinho@gmail.com",
    "b": "b.@gmail.com"
}

#print(dicionario["Kaua"]) #Ele imprime o valor da chave "Kaua", no caso, meu email
#print(dicionario.get("Kaua", "Nome não encontrado"))
#print(dicionario.get("Lula", "Nome não encontrado"))
#print(dicionario["Lula"]) #Como o email não foi cadastrado, o valor de lula será "Nome não encontrado"

#Como modificar valores:
#print(dicionario["b"])
#dicionario["b"] = "bunda@gmail.com"
#print(dicionario["b"])

#print(dicionario.get("Clara", "Nome não encontrado"))
#dicionario["Clara"] = "clara@gmail.com"
#print(dicionario["Clara"])

#Como deletar coisas no dicionário
#del dicionario["b"] #Deleta b
#print(dicionario.pop("b", "Nome não encontrado"))

for chave, valor in dicionario.items():
    print(chave, valor)
    
