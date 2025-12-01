from typing import List
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_box_by_target(
    df: pd.DataFrame,
    columns: List[str],
    target: str,
    n_cols: int = 3,
) -> None:
    '''
    Dibuja boxplots de varias columnas numéricas, separadas por la variable objetivo.
    '''
    n_plots = len(columns)
    n_rows = (n_plots + n_cols - 1) // n_cols

    plt.figure(figsize=(5 * n_cols, 4 * n_rows))

    for i, col in enumerate(columns, start=1):
        plt.subplot(n_rows, n_cols, i)
        sns.boxplot(data=df, x=target, y=col)
        plt.title(f"{col} by {target}")
        plt.xlabel(target)
        plt.ylabel(col)

    plt.tight_layout()
    plt.show()


def plot_violin_with_swarm(
    df: pd.DataFrame,
    column: str,
    target: str
) -> None:
    '''
    Dibuja un gráfico de violín de `column` por `target`
    y encima un swarmplot para ver los puntos individuales.
    '''
    plt.figure(figsize=(8, 5))
    sns.violinplot(
        data=df,
        x=target,
        y=column,
        inner=None,
    )
    sns.swarmplot(
        data=df,
        x=target,
        y=column,
        color="k",
        size=2,
        alpha=0.6,
    )
    plt.title(f"Violin + swarmplot of {column} by {target}")
    plt.tight_layout()
    plt.show()

