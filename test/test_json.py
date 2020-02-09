import unittest
from app import app


class MyTestCase(unittest.TestCase):
    def test_good_json(self):
        """
        Test a valid departure URL and assert the JSON length is > 0
        """
        tester = app.test_client(self)
        response = tester.get('/departures/EUS', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

    def test_bad_json(self):
        """
        Test an invalid departure URL and assert HTTP 400 (HTTPError)
        """
        tester = app.test_client(self)
        response = tester.get('/departures/111', content_type='application/json')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
