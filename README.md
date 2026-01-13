# 
# 0.1 — Crear y activar entorno virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 0.2 — requirements.txt
cat > requirements.txt << 'EOF'
pandas
scikit-learn
joblib
fastapi
uvicorn
pytest
EOF

# 0.3 — .gitignore
cat > .gitignore << 'EOF'
# Entorno
.venv/
# Modelos y cachés
models/
__pycache__/
# Datos locales
data/
EOF

pip install -r requirements.txt
