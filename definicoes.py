

class Raca:
    def __init__(self, nome, movimento, infravisao, alinhamento, habilidades):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = habilidades

class Classe:
    def __init__(self, nome, requisitos, tabela_progressao, permissoes_equip, habilidades_por_nivel):
        self.nome = nome
        self.requisitos = requisitos
        self.tabela_progressao = tabela_progressao
        self.permissoes_equip = permissoes_equip
        self.habilidades_por_nivel = habilidades_por_nivel