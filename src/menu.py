import pandas as pd
from arquivo import listaArquivosDisponiveis, importaArquivo, exportaArquivo
from estatisticas import (
    totalMonitorias,
    alunosUnicos,
    porCurso,
    porDisciplina,
    porBolsista,
    porTurma,
    porHorario,
)
from utils import lerInteiro, limparTerminal, formatarTabela

OPCOES_ESTATISTICAS = {
    1: ("Total de monitorias", totalMonitorias),
    2: ("Alunos únicos", alunosUnicos),
    3: ("Por curso", porCurso),
    4: ("Por disciplina", porDisciplina),
    5: ("Por bolsista", porBolsista),
    6: ("Por turma", porTurma),
    7: ("Por horário", porHorario),
}

def menuInicial() -> int:
    limparTerminal()
    print("=== Menu Inicial ===")
    print("1. Trocar arquivo")
    print("2. Estatisticas")
    print("0. Sair")
    return lerInteiro("Escolha uma opção: ")

def menuSelecaoArquivo() -> pd.DataFrame | None:
    while True:
        arquivos = listaArquivosDisponiveis()

        limparTerminal()
        print("=== Selecione o arquivo ===")
        for indice, nome in enumerate(arquivos, start=1):
            print(f"{indice}. {nome}")
        print("0. Sair")

        escolha = lerInteiro("Digite o número do arquivo: ")
        if escolha == 0:
            return None

        if escolha < 1 or escolha > len(arquivos):
            print("Opção inválida.")
            continue

        df = importaArquivo(arquivos[escolha - 1])
        if df is None:
            print("Arquivo inválido: colunas não correspondem ao esperado.")
            continue

        return df

def menuEstatisticas(df: pd.DataFrame):
    while True:
        limparTerminal()
        print("=== Estatísticas ===")
        for numero, (nome, _) in OPCOES_ESTATISTICAS.items():
            print(f"{numero}. {nome}")
        print("0. Voltar")

        escolha = lerInteiro("Escolha uma opção: ")
        if escolha == 0:
            return

        if escolha not in OPCOES_ESTATISTICAS:
            print("Opção inválida.")
            continue

        nome, funcao = OPCOES_ESTATISTICAS[escolha]
        resultado = funcao(df)

        limparTerminal()
        print(f"=== {nome} ===\n")
        print(formatarTabela(resultado))
        print()

        print("1. Exportar para Excel")
        print("2. Exportar para CSV")
        print("0. Voltar")

        escolhaExportar = lerInteiro("Escolha uma opção: ")
        nomeBase = nome.lower().replace(" ", "_")

        if escolhaExportar == 1:
            caminho = exportaArquivo(resultado, nomeBase, "xlsx")
            print(f"Exportado para {caminho}")
        elif escolhaExportar == 2:
            caminho = exportaArquivo(resultado, nomeBase, "csv")
            print(f"Exportado para {caminho}")
