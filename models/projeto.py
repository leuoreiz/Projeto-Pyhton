
from models.personagem import Personagem
import geracao_atributos
import batalha

def main():
    
    print("Bem-vindo ao Criador de Personagens de RPG!")
    

    nome = input("Digite o nome do seu personagem: ")
    
    print("\nEscolha sua classe:")
    print("[1] Guerreiro")
    print("[2] Ladrão")
    print("[3] Mago")
    escolha = input(">> ")
    
    classes = {"1": "Guerreiro", "2": "Ladrão", "3": "Mago"}
    classe = classes.get(escolha, "Guerreiro") 
    print(f"Classe escolhida: {classe}")

    print("\nEscolha sua raça:")
    print("[1] Humano") 
    print("[2] Elfo")
    print("[3] Anão")
    escolha = input(">> ")
    raca = {"1": "Humano", "2": "Elfo", "3": "Anão"}
    raca = raca.get(escolha, "Humano")
    print(f"Raça escolhida: {raca}")

 
    meu_personagem = Personagem(nome, classe, raca)

    # --- Passo 3: Rolar os atributos finais ---
    print("--- Agora vamos rolar os atributos finais ---")
    modo = input("Escolha o modo de rolagem [1] Clássico | [2] Heroico | [3] Aventureiro:\n>> ")

    atributos_finais = None 
    if modo == "1":
        atributos_finais = geracao_atributos.gerar_atributos_classico()
    elif modo == "2":
        atributos_finais = geracao_atributos.gerar_atributos_heroico()
    elif modo == "3":
        atributos_finais = geracao_atributos.gerar_atributos_aventureiro()
    else:
        print("Opção inválida! Seus atributos base serão mantidos.")

    
    if atributos_finais:
        meu_personagem.atributos = atributos_finais
    
    print("\nParabéns! Criação finalizada.")
    meu_personagem.mostrar_ficha()

    print("Deseja andar? 1 - Sim | 2 - Não")
    andar = input(">> ")
    if andar == "1":
        print("Você começou a andar pelo mundo...")
        print("Um inimigo apareceu!")
        batalha.batalhas(meu_personagem)
    elif andar == "2":
        print("Você decidiu não andar por enquanto.")
    
if __name__ == "__main__":
    main()