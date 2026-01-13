
import joblib

def predecir(texto):
    modelo = joblib.load("modelos/modelo.joblib")
    return modelo.predict([texto])[0]
  
