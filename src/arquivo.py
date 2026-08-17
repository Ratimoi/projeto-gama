import pandas as pd
from pathlib import Path

PASTA_DADOS = Path(__file__).resolve().parent.parent / "data"
EXTENSOES_SUPORTADAS = {".csv", ".xlsx"}
CAMPOS_ESPERADOS = {
    "Carimbo de data/hora",
    "Horário do atendimento",
    "E-mail",
    "Curso",
    "Em caso de outro, especifique o curso",
    "CPF (Apenas números)",
    "Número de Matrícula",
    "Nome Completo (em letras maiúsculas e sem abreviaturas)",
    "Disciplina de matemática que está cursando",
    "Em caso de outro, especifique a disciplina",
    "Turma da disciplina que está cursando (Ex. M1, T1)",
    "Nome do Bolsista",
}

def listaArquivosDisponiveis() -> list[str]:
    return sorted(
        arquivo.name
        for arquivo in PASTA_DADOS.iterdir()
        if arquivo.suffix.lower() in EXTENSOES_SUPORTADAS
    )

def importaArquivo(caminho: str) -> pd.DataFrame | None:
    caminhoCompleto = PASTA_DADOS / caminho
    extensao = identificaArquivo(caminhoCompleto)

    if extensao == ".csv":
        df = pd.read_csv(caminhoCompleto)
    else:
        df = pd.read_excel(caminhoCompleto)

    if not validaArquivo(df):
        return None

    return df

def identificaArquivo(caminho: str) -> str:
    return Path(caminho).suffix.lower()

def validaArquivo(df: pd.DataFrame) -> bool:
    return set(df.columns) == CAMPOS_ESPERADOS

def exportaArquivo():
    return
