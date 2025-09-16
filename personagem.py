import random

class Personagem:
    def __init__(self, nome, classe, raca):
        
        self.nome = nome
        self.classe = classe
        self.raca = raca
        self.nivel = 1
        
        


    def mostrar_ficha(self):
        """Imprime a ficha do personagem de forma organizada."""
        print("\n--- FICHA DO PERSONAGEM ---")
        print(f"Nome:   {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Raça:   {self.raca}")
        print(f"Nível:  {self.nivel}")
        print("---------------------------")
        print("Atributos:")
        for chave, valor in self.atributos.items():
            print(f"  {chave:<15}: {valor}")
        print("---------------------------\n")

    def atacar(self, alvo):
        dano = self.classe.ataque + random.randint(1, 6)
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= (self.classe.defesa - dano) 
        print(f"Você recebeu {dano} de dano e tem {self.vida} de vida restante.")

    def esta_vivo(self):
        return self.vida > 0