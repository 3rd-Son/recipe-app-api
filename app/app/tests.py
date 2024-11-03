from django.test import SimpleTestCase

from app import calc


class Calctests(SimpleTestCase):
    def test_calculation(self):
        res = calc.summit(2, 2)
        self.assertEqual(res, 4)
