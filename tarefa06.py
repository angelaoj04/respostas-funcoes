def converteHora(hora):
    if hora <= 12:
        novaHora = hora
    else:
        novaHora = hora - 12
    return novaHora

def imprimeHora(hora, minutos):
    novaHora = converteHora(hora)
    if novaHora < 12:
        return str(novaHora)+":"+str(minutos)+" AM"
    else:
        return str(novaHora)+":"+str(minutos)+" PM"


converte = "S"

while(converte == "S"):
    converte = input("Deseja converter um horário? S (SIM) N (NÃO): ")
    if(converte.upper() == "S"):
        hora = int(input("Informe a hora: "))
        minutos = int(input("Informe os minutos: "))

        horaConvertida = imprimeHora(hora, minutos)
        print("A hora convertida foi: ", horaConvertida)