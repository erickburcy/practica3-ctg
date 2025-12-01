from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_density_by_class(
    df: pd.DataFrame,
    column: str,
    target: str
) -> None:
    '''
    Dibuja curvas de densidad (KDE) de `column` separadas por los valores de `target`.
    '''
    plt.figure(figsize=(8, 5))
    for level in df[target].dropna().unique():
        subset = df[df[target] == level]
        sns.kdeplot(
            data=subset,
            x=column,
            label=f"{target}={level}",
            fill=True,
            alpha=0.3,
        )
    plt.title(f"Density of {column} by {target}")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_line_series(
    df: pd.DataFrame,
    column: str,
    sort_by: Optional[str] = None
) -> None:
    '''
    Dibuja un gráfico de líneas simple de `column`.
    Opcionalmente ordena por la columna `sort_by`.
    '''
    tmp = df.copy()
    if sort_by is not None:
        tmp = tmp.sort_values(by=sort_by)

    plt.figure(figsize=(8, 5))
    plt.plot(tmp[column].values, marker="o")
    xlabel = "Index"
    if sort_by is not None:
        xlabel += f" (sorted by {sort_by})"
    plt.xlabel(xlabel)
    plt.ylabel(column)
    plt.title(f"Line plot of {column}")
    plt.tight_layout()
    plt.show()


def plot_dot_comparison(
    df: pd.DataFrame,
    column: str,
    group: str
) -> None:
    '''
    Dibuja un dot plot (stripplot) para comparar la distribución de `column`
    entre los grupos definidos por `group`.
    '''
    plt.figure(figsize=(8, 5))
    sns.stripplot(
        data=df,
        x=group,
        y=column,
        jitter=True,
        alpha=0.6,
    )
    plt.title(f"Dot plot of {column} by {group}")
    plt.tight_layout()
    plt.show()

