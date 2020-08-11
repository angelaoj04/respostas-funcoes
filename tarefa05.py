
def somaImposto(taxaImposto, custo):
    valorReajustado = (custo * taxaImposto) + custo
    return valorReajustado

novoValor = somaImposto(0.05, 1000)

print("O valor do produto reajustado é: ",novoValor)
