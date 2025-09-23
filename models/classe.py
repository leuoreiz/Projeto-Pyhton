from models.definicoes import Classe


Guerreiro = Classe(
    nome = "Guerreiro", vida = 10, ataque = 1, defesa = 5, xp = 0
)

Ladrao = Classe(
    nome = "Ladrão", vida = 6, ataque = 1, defesa = 5, xp = 0 
)

Mago = Classe(
    nome = "Mago", vida = 4, ataque = 0, defesa = 5, xp = 0 )

CLASSES_DISPONIVEIS = {
    "1": Guerreiro,
    "2": Ladrao,
    "3": Mago
}