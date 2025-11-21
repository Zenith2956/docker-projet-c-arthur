import os
import random
from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Config from env
DB_HOST = os.getenv("DATABASE_HOST", "db")
DB_PORT = os.getenv("DATABASE_PORT", "3306")
DB_USER = os.getenv("DATABASE_USER", "banduser")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "bandpass")
DB_NAME = os.getenv("DATABASE_NAME", "bandnamesdb")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"

app = Flask(__name__)

def get_engine():
    return create_engine(DATABASE_URL, pool_pre_ping=True)

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    bandnames = []
    try:
        engine = get_engine()
    except Exception as e:
        engine = None
        # Si la creation de engine ne fonctionne pas
    if request.method == "POST":
        action = request.form.get("action")
        if action == "check":
            # verification de la connection à la base de donnée
            try:
                with engine.connect() as conn:
                    conn.execute(text("SELECT 1"))
                message = "Communication avec la base de données établie"
            except SQLAlchemyError:
                message = "Impossible de se connecter à la base de données"
        elif action == "generate":
            # Récupérer les adjectifs et les noms
            try:
                with engine.connect() as conn:
                    adj_rows = conn.execute(text("SELECT adjective FROM adjectives")).fetchall()
                    noun_rows = conn.execute(text("SELECT name FROM nouns")).fetchall()
                adjectives = [r[0] for r in adj_rows]
                nouns = [r[0] for r in noun_rows]
                if not adjectives or not nouns or len(adjectives) < 1 or len(nouns) < 1:
                    message = "Impossible de générer : données insuffisantes en base."
                else:
                    # Génère 10 noms de bandes
                    for _ in range(10):
                        a = random.choice(adjectives)
                        n = random.choice(nouns)
                        bandnames.append(f"The {a} {n}")
            except SQLAlchemyError:
                message = "Impossible de se connecter à la base de données"
    return render_template("index.html", message=message, bandnames=bandnames)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)