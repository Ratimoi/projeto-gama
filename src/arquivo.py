import pandas as pd
from pathlib import Path
from datetime import datetime

PASTA_DADOS = Path(__file__).resolve().parent.parent / "data"
PASTA_EXPORTS = Path(__file__).resolve().parent.parent / "exports"
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

def exportaArquivo(df: pd.DataFrame, nomeBase: str, formato: str) -> Path:
    PASTA_EXPORTS.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho = PASTA_EXPORTS / f"{nomeBase}_{timestamp}.{formato}"

    if formato == "csv":
        df.to_csv(caminho, index=False)
    else:
        df.to_excel(caminho, index=False)

    return caminho
