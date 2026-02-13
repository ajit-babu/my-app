import unittest
from app import app, calculate_sum, calculate_product


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        self.assertEqual(self.app.get("/").status_code, 200)

    def test_health(self):
        self.assertEqual(self.app.get("/health").status_code, 200)

    def test_info(self):
        self.assertEqual(self.app.get("/info").status_code, 200)

    def test_sum(self):
        self.assertEqual(calculate_sum(2, 3), 5)

    def test_product(self):
        self.assertEqual(calculate_product(2, 3), 6)


if __name__ == "__main__":
    unittest.main()
