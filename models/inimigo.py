from models.personagem import Personagem
from classe import Guerreiro, Ladrao, Mago
from models.raca import Humano, Elfo, Anao
import random
import geracao_atributos

def gerar_inimigo(nivel):
    nomes = ["Goblin", "Orc", "Troll"]
    nome = random.choice(nomes)
    classe = random.choice([Guerreiro, Ladrao, Mago])
    raca = random.choice([Humano, Elfo, Anao])

    inimigo = Personagem(nome, classe.nome, raca.nome)
    inimigo.atributos = geracao_atributos.gerar_atributos_classico()

def atacar(self, alvo):
    dano = self.classe.ataque - alvo.classe.defesa
    dano = max(dano, 0)  # Dano mínimo é 0
    alvo.vida -= dano
    return dano