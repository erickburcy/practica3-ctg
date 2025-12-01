import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_horizontal_bar(
    df: pd.DataFrame,
    column: str
) -> None:
    '''
    Dibuja un gráfico de barras horizontal para la columna categórica indicada,
    ordenado por frecuencia.
    '''
    counts = df[column].value_counts()

    plt.figure(figsize=(8, 5))
    sns.barplot(
        x=counts.values,
        y=counts.index,
        orient="h",
    )
    plt.xlabel("Frequency")
    plt.ylabel(column)
    plt.title(f"Horizontal bar plot of {column}")
    plt.tight_layout()
    plt.show()

