import pytest

from app import app, db

from app.models import User, Transaction
 
@pytest.fixture

def app_context():

    # Configure app for testing with in-memory SQLite

    app.config['TESTING'] = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():

        db.create_all()

        yield

        db.session.remove()

        db.drop_all()
 
@pytest.fixture

def user_instance(app_context):

    user = User(username='testuser')

    db.session.add(user)

    db.session.commit()

    return user
 
def test_add_health_points(user_instance):

    initial_total = user_instance.total_points

    initial_health = user_instance.health_points
 
    user_instance.add_points('health', 15, 'exercise')
 
    assert user_instance.health_points == initial_health + 15

    assert user_instance.total_points == initial_total + 15
 
    tx = Transaction.query.filter_by(user_id=user_instance.id, category='health').first()

    assert tx is not None

    assert tx.amount == 15

    assert tx.reason == 'exercise'
 
 
def test_add_energy_points(user_instance):

    initial_total = user_instance.total_points

    initial_energy = user_instance.energy_points
 
    user_instance.add_points('energy', -20, 'fatigue')
 
    assert user_instance.energy_points == initial_energy - 20

    assert user_instance.total_points == initial_total - 20
 
    tx = Transaction.query.filter_by(user_id=user_instance.id, category='energy').first()

    assert tx.amount == -20

    assert tx.reason == 'fatigue'
 
 
def test_repr_user(user_instance):

    r = repr(user_instance)

    assert f'<User {user_instance.username}' in r
 
 
def test_repr_transaction():

    tx = Transaction(user_id=1, category='test', amount=5, reason='raison')

    r = repr(tx)

    assert '<Transaction test: 5 points (raison)' in r

 
