import inimigo

def batalhas(jogador):
    inimigo_gerado = inimigo.gerar_inimigo(nivel=1)
    print(f"\nUm {inimigo_gerado.nome} apareceu!\n")

    while jogador.vida > 0 and inimigo_gerado.vida > 0:
        acao = input("Escolha sua ação: [1] Atacar | [2] Fugir\n>> ")

        if acao == "1":
            jogador.atacar(inimigo_gerado)

            if inimigo_gerado.vida <= 0:
                print("Você derrotou o inimigo!")
                if(jogador.raca.nome == "Humano"):
                    xp_ganho = 11
                    print("você ganhou 11 de xp por ser humano")
                    jogador.xp += xp_ganho
                else: 
                    xp_ganho = 10 
                    print("você ganhou 10 de xp")
                    jogador.xp += xp_ganho
                
                break

            inimigo_gerado.atacar(jogador)
            if jogador.vida <= 0:
                print("Você foi derrotado!")
                break

        elif acao == "2":
            print("Você fugiu da batalha!")
            break
        else:
            print("Ação inválida, tente novamente.")
