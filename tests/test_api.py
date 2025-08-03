import unittest
from application import create_app, db

class UserApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_health_check(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User API is running', response.data)

    def test_create_user(self):
        payload = {
            "name": "Alice",
            "email": "alice@example.com",
            "password": "password123"
        }
        response = self.client.post('/users', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Alice', response.data)

    def test_login_success(self):
        # Create user
        self.client.post('/users', json={
            "name": "Bob",
            "email": "bob@example.com",
            "password": "secret123"
        })
        # Login
        response = self.client.post('/login', json={
            "email": "bob@example.com",
            "password": "secret123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)

    def test_login_failure(self):
        response = self.client.post('/login', json={
            "email": "ghost@example.com",
            "password": "wrongpass"
        })
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
