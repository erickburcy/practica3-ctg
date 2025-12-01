import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlation_heatmap(
    df: pd.DataFrame,
    method: str = "pearson"
) -> None:
    '''
    Dibuja un heatmap de la matriz de correlación de las columnas numéricas.
    '''
    num_df = df.select_dtypes(include="number")
    corr = num_df.corr(method=method)

    plt.figure(figsize=(10, 8))
    sns.heatmap(
        corr,
        annot=False,
        cmap="coolwarm",
        center=0,
        square=True,
    )
    plt.title(f"Correlation heatmap ({method})")
    plt.tight_layout()
    plt.show()

