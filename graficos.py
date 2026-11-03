from pathlib import Path

import matplotlib.pyplot as plt

SALIDA = Path(__file__).parent / "Data" / "processed" / "graficos"


def grafico_ventas_por_categoria(df):
    datos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    SALIDA.mkdir(parents=True, exist_ok=True)
    ax = datos.plot(kind="bar", color="steelblue")
    ax.set_title("Ingresos por categoría")
    ax.set_xlabel("Categoría")
    ax.set_ylabel("Ingresos ($)")
    plt.tight_layout()
    plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight")
    plt.show()
    plt.close()
    print(f"Gráfico guardado en: {SALIDA / 'ventas_por_categoria.png'}")


def grafico_ventas_por_canal(df):
    datos = df.groupby("canal")["total"].sum().sort_values(ascending=False)
    SALIDA.mkdir(parents=True, exist_ok=True)
    ax = datos.plot(kind="bar", color="darkorange")
    ax.set_title("Ingresos por canal")
    ax.set_xlabel("Canal")
    ax.set_ylabel("Ingresos ($)")
    plt.tight_layout()
    plt.savefig(SALIDA / "ventas_por_canal.png", bbox_inches="tight")
    plt.show()
    plt.close()
    print(f"Gráfico guardado en: {SALIDA / 'ventas_por_canal.png'}")


def graficar(df):
    grafico_ventas_por_categoria(df)
    grafico_ventas_por_canal(df)
