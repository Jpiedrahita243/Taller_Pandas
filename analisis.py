import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)


def ingresos_por_categoria(df):
    """Imprime ingresos sumados por categoría y la categoría líder."""
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print("\n1. Ingresos por categoría:")
    print(ingresos.to_string())
    if not ingresos.empty:
        print(f"Categoría con más ingresos: {ingresos.index[0]} (${ingresos.iloc[0]:,.0f}).")


def canal_que_mas_vende(df):
    """Imprime ventas e ingresos por canal y señala el canal con más ventas."""
    resumen = df.groupby("canal").agg(ventas=("id_venta", "count"), ingresos=("total", "sum")).sort_values("ventas", ascending=False)
    print("\n2. Ventas e ingresos por canal:")
    print(resumen.to_string())
    if not resumen.empty:
        print(f"Canal con más ventas: {resumen.index[0]} ({resumen.iloc[0]['ventas']} ventas).")


def clientes_vip_vs_regular(df):
    """Compara número de clientes, compras y gasto promedio por cliente."""
    resumen = df.groupby("segmento_cliente").agg(
        clientes=("id_cliente", "nunique"), compras=("id_venta", "count"), gasto_total=("total", "sum")
    )
    resumen["compras_promedio_por_cliente"] = resumen["compras"] / resumen["clientes"]
    resumen["gasto_promedio_por_cliente"] = resumen["gasto_total"] / resumen["clientes"]
    print("\n3. Compras y gasto promedio por cliente según segmento:")
    print(resumen.to_string())
    if {"VIP", "Regular"}.issubset(resumen.index):
        vip = resumen.loc["VIP"]
        regular = resumen.loc["Regular"]
        respuesta = "Sí" if vip["compras_promedio_por_cliente"] > regular["compras_promedio_por_cliente"] else "No"
        print(f"¿Los clientes VIP compran más que los Regulares? {respuesta}.")


def metodo_pago_mas_usado(df):
    """Imprime el conteo por método de pago e identifica el más usado."""
    conteo = df["metodo_pago"].value_counts()
    print("\n4. Uso de métodos de pago:")
    print(conteo.to_string())
    if not conteo.empty:
        print(f"Método más usado: {conteo.index[0]} ({conteo.iloc[0]} compras).")


def top5_clientes(df):
    """Imprime los cinco clientes con más compras (gasto como desempate)."""
    top = (
        df.groupby(["id_cliente", "nombre_cliente"])
        .agg(compras=("id_venta", "count"), gasto_total=("total", "sum"))
        .sort_values(["compras", "gasto_total"], ascending=[False, False])
        .head(5)
    )
    print("\n5. Cinco clientes con más compras:")
    print(top.to_string())
