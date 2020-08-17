#JOGAR DADOS
def jogar():
    jogada = random.randint(2,12)
    return jogada

#jogo
quantidade_de_jogadas = 1
termina = False
ponto = 0

while not termina:
    jogada = jogar()
    if quantidade_de_jogadas == 1:
        if jogada == 7 or jogada == 1:
            print("Parabéns! Você é um natural e você ganhou!")
            termina = True
        elif jogada == 2 or jogada == 3 or jogada == 12:
            print(" CRAPS! Você perdeu!")
            termina = True
        elif jogada >= 4 and jogada <=10:
            ponto = jogada
            print(f"{jogada}: Este é o seu ponto! Você deve tentar tirá-lo novamente, "
                  f"mas se tirar o 7 você perde!")
    else:
        if jogada == ponto:
            print("Parabéns! Você ganhou!")
            termina = True
        elif jogada == 7:
            print(f"CRAPS! Você perdeu!")
            termina = True
        else:
            print("Tente novamente!")
    quantidade_de_jogadas += 1