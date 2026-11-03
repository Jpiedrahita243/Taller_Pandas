from pathlib import Path

import pandas as pd

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    """Valida las claves y reporta ventas sin cliente asociado."""
    correcto = True
    for nombre, df in (("clientes", clientes), ("ventas", ventas)):
        if "id_cliente" not in df.columns:
            print(f"Error: falta la columna id_cliente en {nombre}.")
            correcto = False

    if not correcto:
        return False

    if clientes["id_cliente"].duplicated().any():
        cantidad = int(clientes["id_cliente"].duplicated().sum())
        print(f"Error: id_cliente está repetido en clientes ({cantidad} duplicados).")
        correcto = False
    else:
        print("Validación: id_cliente no está repetido en clientes.")

    tipo_clientes = clientes["id_cliente"].dtype
    tipo_ventas = ventas["id_cliente"].dtype
    if tipo_clientes != tipo_ventas:
        print(f"Error: tipos distintos para id_cliente: clientes={tipo_clientes}, ventas={tipo_ventas}.")
        correcto = False
    else:
        print(f"Validación: id_cliente tiene el mismo tipo en ambas tablas ({tipo_clientes}).")

    ids_cliente = clientes["id_cliente"].dropna().unique()
    sin_cliente = int((~ventas["id_cliente"].isin(ids_cliente)).sum())
    print(f"Ventas sin cliente asociado: {sin_cliente} (se conservan con merge left).")
    return correcto


def unir(clientes, ventas):
    """Valida, une ventas con clientes y guarda Data/processed/merge.csv."""
    if not validar_premerge(clientes, ventas):
        print("No se realizó el merge: corrige las validaciones indicadas.")
        return None

    df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")
    PROCESSED.mkdir(parents=True, exist_ok=True)
    ruta = PROCESSED / "merge.csv"
    df.to_csv(ruta, index=False)
    print(f"Merge realizado: {df.shape[0]} filas y {df.shape[1]} columnas.")
    print(f"Archivo guardado en: {ruta}")
    print(df.head())
    return df
