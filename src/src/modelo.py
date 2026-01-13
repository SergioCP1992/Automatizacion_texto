
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def crear_modelo():
    return Pipeline([
        ("vectorizador", TfidfVectorizer(stop_words="spanish")),
        ("clasificador", LogisticRegression(max_iter=1000))
    ])
