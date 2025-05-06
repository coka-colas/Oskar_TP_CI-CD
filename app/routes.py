from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User, Transaction

# Affichage du HTML
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


# Ici est le squelette du questionnaire qui est posé au joueur (on demande son pseudo, puis quelle catégorie de points, 
# puis le nombre gagné ou perdu, puis la raison de cette perte ou de ce gain
@app.route('/add', methods=['POST'])
def add_points():
    username = request.form.get('username')
    category = request.form.get('category')
    points = int(request.form.get('points'))
    reason = request.form.get('reason')

    user = User.query.filter_by(username=username).first()
    
# S'il n'existe pas on l'ajoute dans la BDD
    if not user:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()

# On fait le calcul
    user.add_points(category, points, reason)

    return redirect(url_for('index'))

# Permet de conserver l'historique
@app.route('/history/<username>')
def history(username):
    user = User.query.filter_by(username=username).first_or_404()
    transactions = Transaction.query.filter_by(user_id=user.id).order_by(Transaction.timestamp.desc()).all()
    return render_template('history.html', user=user, transactions=transactions)
