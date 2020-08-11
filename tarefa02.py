def imprimir(numero):
    parada_i = numero + 1
    resposta = ""
    for i in range(1, parada_i):
        parada_j = i + 1
        for j in range(1, parada_j):
            resposta = resposta + str(j) +" "
        resposta = resposta +"\n"
    print(resposta)

numero = int(input("Digite um número: "))

imprimir(numero)