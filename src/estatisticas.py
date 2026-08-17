import unicodedata
import pandas as pd

def removerAcentos(texto: str) -> str:
    return "".join(
        caractere
        for caractere in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caractere) != "Mn"
    )

def contagemPorCampo(df: pd.DataFrame, campo: str) -> pd.DataFrame:
    return (
        df[campo]
        .astype(str)
        .str.strip()
        .str.lower()
        .map(removerAcentos)
        .str.replace(r"\s+", " ", regex=True)
        .value_counts()
        .rename_axis(campo)
        .reset_index(name="Quantidade")
    )

def porCurso(df: pd.DataFrame) -> pd.DataFrame:
    return contagemPorCampo(df, "Curso")

def porDisciplina(df: pd.DataFrame) -> pd.DataFrame:
    return contagemPorCampo(df, "Disciplina de matemática que está cursando")

def porBolsista(df: pd.DataFrame) -> pd.DataFrame:
    resultado = contagemPorCampo(df, "Nome do Bolsista")
    resultado["Nome do Bolsista"] = resultado["Nome do Bolsista"].str.title()
    return resultado

def porTurma(df: pd.DataFrame) -> pd.DataFrame:
    return contagemPorCampo(df, "Turma da disciplina que está cursando (Ex. M1, T1)")

def porHorario(df: pd.DataFrame) -> pd.DataFrame:
    return contagemPorCampo(df, "Horário do atendimento")

def totalMonitorias(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"Total de monitorias": [len(df)]})

def alunosUnicos(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"Alunos únicos": [df["Número de Matrícula"].nunique()]})
