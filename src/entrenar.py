
from src.cargar_datos import cargar_datos
from src.modelo import crear_modelo
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

def entrenar():
    datos = cargar_datos()
    X = datos["texto"]
    y = datos["etiqueta"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = crear_modelo()
    modelo.fit(X_train, y_train)

    predicciones = modelo.predict(X_test)
    print("=== Métricas ===")
    print(classification_report(y_test, predicciones))

    os.makedirs("modelos", exist_ok=True)
    joblib.dump(modelo, "modelos/modelo.joblib")
    print("Modelo guardado en modelos/modelo.joblib")

if __name__ == "__main__":
    entrenar()
