from typing import Tuple
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer


def drop_high_null_columns(df: pd.DataFrame, threshold: float = 0.2) -> pd.DataFrame:
    '''
    Elimina columnas con más de `threshold` proporción de nulos.
    '''
    null_ratio = df.isna().mean()
    cols_to_keep = null_ratio[null_ratio <= threshold].index
    return df[cols_to_keep].copy()


def impute_missing_simple(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Imputa nulos usando media/mediana para numéricas y moda para categóricas.
    '''
    df_imputed = df.copy()

    for col in df_imputed.columns:
        col_data = df_imputed[col]

        if pd.api.types.is_numeric_dtype(col_data):
            skewness = col_data.skew(skipna=True)
            if abs(skewness) < 1:
                value = col_data.mean(skipna=True)
            else:
                value = col_data.median(skipna=True)
        else:
            mode_vals = col_data.mode(dropna=True)
            value = mode_vals.iloc[0] if not mode_vals.empty else None

        df_imputed[col] = col_data.fillna(value)

    return df_imputed


def impute_missing_knn(df: pd.DataFrame, n_neighbors: int = 5) -> pd.DataFrame:
    '''
    Imputa nulos en columnas numéricas usando KNNImputer.
    '''
    df_knn = df.copy()
    num_cols = df_knn.select_dtypes(include="number").columns

    if len(num_cols) == 0:
        return df_knn

    imputer = KNNImputer(n_neighbors=n_neighbors)
    imputed_array = imputer.fit_transform(df_knn[num_cols])
    df_knn[num_cols] = imputed_array

    return df_knn


def detect_outliers_iqr(series: pd.Series) -> pd.Series:
    '''
    Detecta outliers usando la regla IQR.
    '''
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return (series < lower) | (series > upper)


def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    '''
    Detecta outliers usando z-score.
    '''
    mean = series.mean()
    std = series.std(ddof=0)

    if std == 0 or np.isnan(std):
        return pd.Series(False, index=series.index)

    z = (series - mean) / std
    return z.abs() > threshold


def cap_outliers_iqr(series: pd.Series) -> pd.Series:
    '''
    Capea outliers reemplazándolos por los límites IQR.
    '''
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series.clip(lower=lower, upper=upper)

