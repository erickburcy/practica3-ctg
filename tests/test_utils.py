import pandas as pd
from src.ctg_viz import check_data_completeness_tunombrecompleto


def test_check_data_completeness():
    df = pd.DataFrame({
        "a": [1, None, 3],
        "b": ["x", "y", None]
    })

    summary = check_data_completeness_tunombrecompleto(df)

    # Debe contener ambas columnas
    assert "a" in summary.index
    assert "b" in summary.index

    # Debe incluir completitud correcta
    assert summary.loc["a", "completeness"] == 2/3
    assert summary.loc["b", "completeness"] == 2/3

    # Dtype debe ser correcto
    assert summary.loc["a", "dtype"] == "float64" or "int64"
    assert summary.loc["b", "dtype"] == "object"
