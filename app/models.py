from datetime import datetime
from app import db

# On initialise les variables des utilisateurs avec valeurs par défaut
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    total_points = db.Column(db.Integer, default=0)
    health_points = db.Column(db.Integer, default=100)
    energy_points = db.Column(db.Integer, default=100)

    transactions = db.relationship('Transaction', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}, Total: {self.total_points}, Vie: {self.health_points}, Énergie: {self.energy_points}>'

    def add_points(self, category, amount, reason):
        """Ajoute des points avec une explication"""
        if category == "health":
            self.health_points += amount
        elif category == "energy":
            self.energy_points += amount

        self.total_points += amount

        # Ajouter l'historique avec une raison
        new_transaction = Transaction(user_id=self.id, category=category, amount=amount, reason=reason)
        db.session.add(new_transaction)
        db.session.commit()

# Modèle pour l'historique des points
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Transaction {self.category}: {self.amount} points ({self.reason}) at {self.timestamp}>'
