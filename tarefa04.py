def analisa(valor):
    if(valor <= 0):
        return "N"
    else:
        return "P"

resultado = analisa(0)
print("O arguemnto é: ",resultado)