import unittest
from app import app


class MyTestCase(unittest.TestCase):
    def test_json(self):
        tester = app.test_client(self)
        response = tester.get('/EUS', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"train":"LATE!"}\n')


if __name__ == '__main__':
    unittest.main()
