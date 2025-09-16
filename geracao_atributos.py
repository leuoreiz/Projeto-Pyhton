import random
def rolar_dado():
    soma = 0
    for _ in range(3):
        dado = random.randint(1, 6)
        print(f"Você rolou {dado}")
        soma += dado
    return soma
    print(f"Você rolou {dado}")

def rolar_dado_heroico():
    dados = [random.randint(1, 6) for _ in range(4)]
    print(f"Rolagens: {dados}")
    menor = min(dados)
    dados.remove(menor)
    soma = sum(dados)
    return soma

def gerar_atributos_classico():
    print("\nRolando dados para seus atributos (modo clássico)...\n")
    atributos = {
        "Força": rolar_dado(),
        "Inteligência": rolar_dado(),
        "Destreza": rolar_dado(),
        "Constituição": rolar_dado(),
        "Sabedoria": rolar_dado(),
        "Carisma": rolar_dado()
    }
    return atributos

def gerar_atributos_heroico():
    print("\nRolando dados para seus atributos (modo heroico)...\n")
    atributos = {
        "Força": rolar_dado_heroico(),
        "Inteligência": rolar_dado_heroico(),
        "Destreza": rolar_dado_heroico(),
        "Constituição": rolar_dado_heroico(),
        "Sabedoria": rolar_dado_heroico(),
        "Carisma": rolar_dado_heroico()
    }
    return atributos

def gerar_atributos_aventureiro():
    print("\nRolando dados para seus atributos (modo aventureiro)...\n")
    atributos = {
        "Força": 0,
        "Inteligência": 0,
        "Destreza": 0,
        "Constituição": 0,
        "Sabedoria": 0,
        "Carisma": 0
    }

    atributos_lista = list(atributos.keys())

    for i in range(6):
        valor = rolar_dado()
        print(f"\nVocê rolou {valor}.")
        print("Escolha em qual atributo deseja colocar:")
        for idx, nome in enumerate(atributos_lista, 1):
            print(f"{idx}. {nome} (atual: {atributos[nome]})")

        while True:
            escolha = input("Digite o número do atributo: ")
            if escolha.isdigit() and 1 <= int(escolha) <= 6:
                atributo_escolhido = atributos_lista[int(escolha) - 1]
                atributos[atributo_escolhido] += valor
                break
            else:
                print("Escolha inválida, tente novamente.")

    return atributos