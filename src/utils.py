import os
import subprocess
import pandas as pd

def lerInteiro(mensagem: str) -> int:
    while True:
        valor = input(mensagem)
        try:
            return int(valor)
        except ValueError:
            print("Digite um número válido.")

def lerFloat(mensagem: str) -> float:
    while True:
        valor = input(mensagem)
        try:
            return float(valor)
        except ValueError:
            print("Digite um número válido.")

def lerString(mensagem: str) -> str:
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Digite um valor válido.")

def formatarTabela(df: pd.DataFrame) -> str:
    colunas = df.columns
    larguras = {
        coluna: max(len(str(coluna)), df[coluna].astype(str).str.len().max())
        for coluna in colunas
    }

    cabecalho = "  ".join(str(coluna).center(larguras[coluna]) for coluna in colunas)
    linhas = [
        "  ".join(str(valor).center(larguras[coluna]) for coluna, valor in zip(colunas, linha))
        for linha in df.itertuples(index=False)
    ]

    return "\n".join([cabecalho, *linhas])

def limparTerminal():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"])
    else:
        subprocess.run(["clear"])
