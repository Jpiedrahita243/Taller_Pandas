import pandas as pd

from carga import cargar_datos

clientes, ventas = cargar_datos()

print("=== CLIENTES: shape ===")
print(clientes.shape)

print("\n=== CLIENTES: info ===")
clientes.info()

print("\n=== CLIENTES: describe ===")
print(clientes.describe())

print("\n=== VENTAS: shape ===")
print(ventas.shape)

print("\n=== VENTAS: info ===")
ventas.info()

print("\n=== VENTAS: describe ===")
print(ventas.describe())

# Indexación: usamos id_venta como índice
ventas = ventas.set_index("id_venta")

print("\nPrimeras filas con índice id_venta:")
print(ventas.head())

# .loc busca por etiqueta (el ID de venta)
print("\n.loc['V003', 'total']:")
print(ventas.loc["V003", "total"])

# .iloc busca por posición (empieza en 0)
print("\n.iloc[2, 6]:")
print(ventas.iloc[2, 6])

# Rangos: .loc incluye el final; .iloc no
print("\n.loc['V001':'V006'] (por etiqueta, incluye V006):")
print(list(ventas.loc["V001":"V006"].index))

print("\n.iloc[0:5] (por posición, no incluye la posición 5, que es V006):")
print(list(ventas.iloc[0:5].index))

# concat: unir de nuevo las ventas de abril y mayo
ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"])
abril = ventas[ventas["fecha_venta"].dt.month == 4]
mayo = ventas[ventas["fecha_venta"].dt.month == 5]

print("\nFilas de abril:", len(abril), "| filas de mayo:", len(mayo))

total = pd.concat([abril, mayo])
print("Filas tras concat:", len(total), "| filas originales:", len(ventas))