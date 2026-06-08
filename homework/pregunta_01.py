"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    colors = {
        'Television' : 'dimgray',
        'Newspaper' : 'grey',
        'Radio' : 'lightgray',
        'Internet' : 'tab:blue',
    }

    zorder = {
        'Television' : 1,
        'Newspaper' : 1,
        'Radio' : 1,
        'Internet' : 2,
    }

    linewidths = {
        'Television' : 2,
        'Newspaper' : 2,
        'Radio' : 2,
        'Internet' : 4,
    }
    
    df = pd.read_csv("files/input/news.csv", index_col=0)
    os.makedirs("files/plots", exist_ok=True)

    plt.figure(figsize=(10, 6))

    for col in df.columns:
        plt.plot(df[col],
                  color=colors[col],
                  label=col,
                  zorder=zorder[col],
                  linewidth=linewidths[col],
                  )
    
    plt.suptitle("How people get their news",fontsize=16)
    plt.title("An increasing proportion cite the internet as their main primary source", fontsize=12, ha='center')


    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col]
        )
        
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + " " + str(df[col][first_year]) + "%",
            ha = 'right',
            va = 'center',
            color=colors[col],
        )

        plt.text(
            df.index[-1] + 0.2,
            df[col][df.index[-1]],
            str(df[col][df.index[-1]]) + "%",
            ha = 'left',
            va = 'center',
            color=colors[col],
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
            zorder=zorder[col]
        )
    
    plt.xticks(
        ticks = df.index,
        labels = df.index,
        ha = 'center'
    )
    
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.show()

if __name__ == "__main__":
    pregunta_01()