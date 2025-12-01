from typing import Literal, Tuple
import pandas as pd

from .categorization import classify_numeric_columns


def check_data_completeness_Erick_Burciaga(
    df: pd.DataFrame,
    dispersion_stats: Tuple[
        Literal["mean", "median", "std", "min", "max"], ...
    ] = ("mean", "median", "std", "min", "max"),
) -> pd.DataFrame:
    '''
    Genera una tabla resumen con completitud, tipos y estadísticos.

    Por cada columna calcula:
        - null_count
        - completeness (0-1)
        - dtype
        - variable_type ('continuous', 'discrete', 'non-numeric')
        - estadísticos de dispersión (solo numéricas)
    '''
    classification = classify_numeric_columns(df)
    continuous = set(classification["continuous"])
    discrete = set(classification["discrete"])

    rows = []

    for col in df.columns:
        col_data = df[col]
        null_count = int(col_data.isna().sum())
        completeness = 1 - null_count / len(df)
        dtype = str(col_data.dtype)

        if col in continuous:
            var_type = "continuous"
        elif col in discrete:
            var_type = "discrete"
        else:
            var_type = "non-numeric"

        if pd.api.types.is_numeric_dtype(col_data):
            stats_values = {
                "mean": float(col_data.mean(skipna=True)),
                "median": float(col_data.median(skipna=True)),
                "std": float(col_data.std(skipna=True)),
                "min": float(col_data.min(skipna=True)),
                "max": float(col_data.max(skipna=True)),
            }
        else:
            stats_values = {name: None for name in dispersion_stats}

        row = {
            "column": col,
            "null_count": null_count,
            "completeness": completeness,
            "dtype": dtype,
            "variable_type": var_type,
        }
        row.update({f"stat_{k}": v for k, v in stats_values.items()})
        rows.append(row)

    summary_df = pd.DataFrame(rows).set_index("column")
    return summary_df

