from definicoes import Raca

Anao = Raca(
    nome="Anão",
    movimento = 6,
    infraviao = 18,
    alinhamento = "ordem"
)

Humano = Raca(
    nome="Humano",
    movimento = 9,
    infraviao = 0,
    alinhamento = "qualquer"
)

Elfo = Raca(
    nome="Elfo",
    movimento = 9,
    infraviao = 18,
    alinhamento = "neutro"
)

RACAS_DISPONIVEIS = {
    "1": Humano,
    "2": Elfo,
    "3": Anao
}