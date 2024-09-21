import unittest
from werkzeug import exceptions

from app import ctx
import app

class GetCodeTestCase(unittest.TestCase):
    def test_happy_get_code(self):
            res = app.get_code().response.pop()
            self.assertEqual(res, b'"Random number or message"\n')

class PlusTestCase(unittest.TestCase):
    def test_happy_plus(self):
        res = app.plus(1, 2).response.pop()
        self.assertEqual(res, b'3\n')
    
    def test_first_num_invalid(self):
        with self.assertRaises(exceptions.BadRequest):
            app.plus(1, "2+9/5")
    
    def test_second_num_invalid(self):
        with self.assertRaises(exceptions.BadRequest):
            app.plus("2+9/5", 5)
    
    def test_both_num_invalid(self):
        with self.assertRaises(exceptions.BadRequest):
            app.plus("2+9/5", "2+9/5")


if __name__ == "__main__":
    with ctx:
        unittest.main()