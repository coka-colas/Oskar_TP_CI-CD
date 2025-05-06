FROM python:3.9

WORKDIR /app

# Copie des fichiers nécessaires pour l'appli & install des dépendances
COPY . /app

RUN pip install -r requirements.txt

# Exposition du port
EXPOSE 5000

# Lancer l'appli via CLI
CMD ["python", "run.py"]