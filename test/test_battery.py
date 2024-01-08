import unittest
from datetime import date
from os.path import dirname, abspath, join
import sys

THIS_DIR = dirname(__file__)
CODE_DIR = abspath(join(THIS_DIR, '..'))
sys.path.append(CODE_DIR)

from serviceable.carparts.Battery import *

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2017-01-25")
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
