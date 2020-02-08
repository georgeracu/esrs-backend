import unittest
from app import app


class BasicTests(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')

    def test_json(self):
        tester = app.test_client(self)
        response = tester.get('/EUS', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"train": "LATE!"})


if __name__ == '__main__':
    unittest.main()
