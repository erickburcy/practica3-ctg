from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram_with_kde(
    df: pd.DataFrame,
    column: str,
    hue: Optional[str] = None,
    bins: int = 30,
    kde: bool = True,
) -> None:
    '''
    Dibuja un histograma de la columna indicada, con KDE opcional
    y agrupando por `hue` si se especifica.
    '''
    plt.figure(figsize=(8, 5))
    sns.histplot(
        data=df,
        x=column,
        hue=hue,
        bins=bins,
        kde=kde,
        stat="density",
        alpha=0.6,
    )
    title = f"Histogram of {column}"
    if hue:
        title += f" by {hue}"
    plt.title(title)
    plt.tight_layout()
    plt.show()

