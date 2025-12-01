import pandas as pd
from src.ctg_viz import classify_numeric_columns


def test_classify_numeric_columns():
    df = pd.DataFrame({
        "cont": list(range(50)),    # 50 valores → continuo
        "disc": [1, 2, 1, 2, 1],   # 2 valores → discreto
        "text": ["a", "b", "a", "b", "c"]
    })

    classes = classify_numeric_columns(df)

    assert "cont" in classes["continuous"]
    assert "disc" in classes["discrete"]
    assert "text" not in classes["continuous"]
    assert "text" not in classes["discrete"]
