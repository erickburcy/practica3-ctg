import pandas as pd
import numpy as np

from src.ctg_viz import (
    drop_high_null_columns,
    impute_missing_simple,
    impute_missing_knn,
    detect_outliers_iqr,
    detect_outliers_zscore,
    cap_outliers_iqr,
)


def test_drop_high_null_columns():
    df = pd.DataFrame({
        "a": [1, 2, None, None],  # 50% nulls
        "b": [1, 2, 3, 4],        # 0% nulls
    })

    df2 = drop_high_null_columns(df, threshold=0.49)

    assert "a" not in df2.columns
    assert "b" in df2.columns


def test_impute_missing_simple():
    df = pd.DataFrame({
        "num": [1, None, 3],
        "cat": ["a", None, "a"]
    })

    df2 = impute_missing_simple(df)

    assert df2.isna().sum().sum() == 0       # no nulos restantes
    assert df2.loc[1, "cat"] == "a"           # moda imputada


def test_impute_missing_knn():
    df = pd.DataFrame({
        "x": [1, 2, np.nan, 4],
        "y": [10, 20, 30, 40]
    })

    df2 = impute_missing_knn(df)

    assert df2.isna().sum().sum() == 0        # no nulos luego de KNN


def test_detect_outliers_iqr():
    s = pd.Series([1, 2, 3, 4, 100])  # 100 es outlier por IQR
    outliers = detect_outliers_iqr(s)
    assert outliers.sum() == 1


def test_detect_outliers_zscore():
    s = pd.Series([1, 2, 3, 4, 100])  # 100 muy lejos de la media
    outliers = detect_outliers_zscore(s, threshold=3.0)
    assert outliers.sum() == 1


def test_cap_outliers_iqr():
    s = pd.Series([1, 2, 3, 4, 100])
    capped = cap_outliers_iqr(s)
    assert capped.max() < 100         # valor recortado
