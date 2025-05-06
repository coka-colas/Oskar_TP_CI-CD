# ATTENTION N'UTILISER QUE SI VOUS VOULEZ SUPPRIMER LA BASE DE DONNEES

from app import app, db

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Base de données réinitialisée.")
