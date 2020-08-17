def valorPagamento(prest, atraso):
    if atraso>0:
        prest = prest + (prest * 0.03) + (prest * 0.1*atraso)
    else:
        prest = prest
    return prest

soma = 0
quantidade = 0
valor_prest = float(input("Informe o valor da prestação: "))
while valor_prest != 0:
    dias = int(input("Informe a quantidade de dias em atraso: "))
    final = valorPagamento(valor_prest, dias)
    print("Valor final a ser pago: ", final)
    soma += final
    quantidade += 1
    valor_prest = float(input("Informe o valor da prestação: "))

print("Relatório do dia:")
print(" Quantidade de prestações : ", quantidade)
print("Valor total recebido: R$", soma)
