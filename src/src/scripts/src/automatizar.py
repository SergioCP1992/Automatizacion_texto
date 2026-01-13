
import os
import shutil
from src.predecir import predecir

def organizar_archivos(carpeta="mensajes_txt"):
    spam_dir = os.path.join(carpeta, "spam")
    no_spam_dir = os.path.join(carpeta, "no_spam")
    os.makedirs(spam_dir, exist_ok=True)
    os.makedirs(no_spam_dir, exist_ok=True)

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            ruta = os.path.join(carpeta, archivo)
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
            etiqueta = predecir(contenido)
            destino = spam_dir if etiqueta == "spam" else no_spam_dir
            shutil.move(ruta, os.path.join(destino, archivo))
            print(f"{archivo} -> {etiqueta}")

if __name__ == "__main__":
    organizar_archivos()
