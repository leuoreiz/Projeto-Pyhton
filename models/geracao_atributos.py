import random


def escolher_atributo(atributos):
    print("\nEscolha em qual atributo deseja colocar:")
    atributos_lista = list(atributos.keys())
    for idx, nome in enumerate(atributos_lista, 1):
        print(f"{idx}. {nome} (atual: {atributos[nome]})")

    while True:
        escolha = input("Digite o número do atributo: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(atributos_lista):
            return atributos_lista[int(escolha) - 1]
        else:
            print("Escolha inválida, tente novamente.")


# --- Funções Auxiliares de Rolagem de Dados ---

def rolar_3d6():
    """Rola 3 dados de 6 lados e retorna a soma."""
    return sum(random.randint(1, 6) for _ in range(3))

def rolar_4d6_drop_lowest():
    """Rola 4 dados de 6 lados, descarta o menor e retorna a soma dos 3 maiores."""
    rolagens = [random.randint(1, 6) for _ in range(4)]
    rolagens.remove(min(rolagens))
    return sum(rolagens)


# --- Funções Principais Usadas pelo app.py ---

def gerar_atributos_classico():
    """Gera um dicionário de atributos com valores fixos (3d6)."""
    print("\nRolando dados para seus atributos (modo clássico)...\n")
    return {
        "Força": rolar_3d6(),
        "Inteligência": rolar_3d6(),
        "Destreza": rolar_3d6(),
        "Constituição": rolar_3d6(),
        "Sabedoria": rolar_3d6(),
        "Carisma": rolar_3d6()
    }

def gerar_atributos_heroico():
    """Gera uma lista com 6 valores (4d6 drop lowest) para serem distribuídos."""
    print("\nRolando dados para seus atributos (modo heroico)...\n")
    return [rolar_4d6_drop_lowest() for _ in range(6)]

def gerar_atributos_aventureiro():
    """Gera uma lista com 6 valores (3d6) para serem distribuídos."""
    print("\nRolando dados para seus atributos (modo aventureiro)...\n")
    return [rolar_3d6() for _ in range(6)]
