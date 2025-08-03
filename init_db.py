from application import create_app, db
from application.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    # Add sample users with hashed passwords
    user1 = User(name="Bhoomika Macha", email="bhoomi@example.com", password=generate_password_hash("hashed123"))
    user2 = User(name="Priyanka Macha", email="priya@example.com", password=generate_password_hash("hashed456"))
    db.session.add_all([user1, user2])
    db.session.commit()
    print("Database initialized with sample data.")
