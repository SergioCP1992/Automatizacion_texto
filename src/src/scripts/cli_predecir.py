
import argparse
from src.predecir import predecir

def main():
    parser = argparse.ArgumentParser(description="Clasificador de mensajes (spam/no_spam)")
    parser.add_argument("texto", type=str, help="Texto a clasificar")
    args = parser.parse_args()
    etiqueta = predecir(args.texto)
    print(f"Predicción: {etiqueta}")

if __name__ == "__main__":
    main()
