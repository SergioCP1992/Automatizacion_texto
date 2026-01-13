
import pandas as pd

def cargar_datos(ruta="data/mensajes.csv"):
    df = pd.read_csv(ruta)
    if not {"texto", "etiqueta"}.issubset(df.columns):
        raise ValueError("El CSV debe tener columnas: 'texto' y 'etiqueta'")
    return df
