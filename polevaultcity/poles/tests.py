import datetime

from django.test import TestCase

from .models import Pole


class PoleModelTests(TestCase):

    def test_pretty_length(self):
        item = Pole(inches=125)
        output = item.pretty_length()
        self.assertEqual(output, "10'5\"")

    def test_age_computes_diff(self):
        old = datetime.datetime(2022, 4, 1)
        new = datetime.datetime(2022, 5, 1)
        item = Pole(purchase_date=old)
        diff = item.age(new)
        self.assertEqual(diff, datetime.timedelta(days=30))
