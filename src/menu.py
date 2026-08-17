from arquivo import listaArquivosDisponiveis, importaArquivo
from utils import lerInteiro

def menuInicial():
    print("=== Menu Inicial ===")
    print("1. Escolher arquivo")
    print("2. Estatisticas")
    print("0. Sair")

def menuSelecaoArquivo():
    while True:
        arquivos = listaArquivosDisponiveis()

        print("=== Selecione o arquivo ===")
        for indice, nome in enumerate(arquivos, start=1):
            print(f"{indice}. {nome}")

        escolha = lerInteiro("Digite o número do arquivo: ")
        if escolha < 1 or escolha > len(arquivos):
            print("Opção inválida.")
            continue

        df = importaArquivo(arquivos[escolha - 1])
        if df is None:
            print("Arquivo inválido: colunas não correspondem ao esperado.")
            continue

        return df

def menuEstatisticas():
    return

def dashboard():
    return
