from typing import Dict, List
import pandas as pd


def classify_numeric_columns(df: pd.DataFrame) -> Dict[str, List[str]]:
    '''
    Clasifica columnas numéricas en continuas o discretas.

    Reglas:
        - Continuous: numéricas con > 10 valores únicos.
        - Discrete: numéricas con <= 10 valores únicos.
    '''
    continuous: List[str] = []
    discrete: List[str] = []

    num_cols = df.select_dtypes(include="number").columns

    for col in num_cols:
        nunique = df[col].nunique(dropna=True)
        if nunique > 10:
            continuous.append(col)
        else:
            discrete.append(col)

    return {"continuous": continuous, "discrete": discrete}

