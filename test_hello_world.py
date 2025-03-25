import unittest
from hello_world import app

class HelloWorldTestCase(unittest.TestCase):
    """Test case for the hello_world Flask app."""

    def setUp(self):
        """Set up the test client."""
        app.testing = True  # Enable testing mode
        self.client = app.test_client()  # Create a test client

    def test_greeting_endpoint(self):
        """Test the /greeting route."""
        response = self.client.get('/greeting')  # Send a GET request
        self.assertEqual(response.status_code, 200)  # Check if response is OK (200)
        self.assertIn(b'Welcome to CI/CD 101 using GitHub Actions!', response.data)  # Check if the greeting is in the response

    def test_html_structure(self):
        """Ensure HTML content is present in the response."""
        response = self.client.get('/greeting')
        self.assertIn(b'<html>', response.data)
        self.assertIn(b'<body>', response.data)
        self.assertIn(b'<div', response.data)
        self.assertIn(b'</html>', response.data)

if __name__ == '__main__':
    unittest.main()
