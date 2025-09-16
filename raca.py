from definicoes import Raca

Anao = Raca(
    nome="Anão",
    movimento = 6,
    infravisao = 18,
    alinhamento = "ordem",
    habilidades=["+1 em resistencia"]
)

Humano = Raca(
    nome="Humano",
    movimento = 9,
    infravisao = 0,
    alinhamento = "qualquer",
    habilidades=["+10% de XP" ]
)

Elfo = Raca(
    nome="Elfo",
    movimento = 9,
    infravisao = 18,
    alinhamento = "neutro",
    habilidades=["+1 em ataques a distancia"]
)

RACAS_DISPONIVEIS = {
    "1": Humano,
    "2": Elfo,
    "3": Anao
}