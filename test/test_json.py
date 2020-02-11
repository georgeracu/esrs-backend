import unittest
from app import app


class MyTestCase(unittest.TestCase):
    def test_good_json(self):
        """Test that the JSON response is OK and length is greater than 0
        """
        tester = app.test_client(self)
        response = tester.get('/departures/EUS', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assert_(len(response.data) > 0)


if __name__ == '__main__':
    unittest.main()
