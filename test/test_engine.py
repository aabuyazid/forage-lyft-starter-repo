import unittest

from os.path import dirname, abspath, join
import sys

THIS_DIR = dirname(__file__)
CODE_DIR = abspath(join(THIS_DIR, '..'))
sys.path.append(CODE_DIR)

from serviceable.carparts.Engine import *

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = SternmanEngine(warning_light_on=True)

        self.assertTrue(engine.needs_service())
        pass

    def test_needs_service_false(self):
        engine = SternmanEngine(warning_light_on=False)

        self.assertFalse(engine.needs_service())
        pass

if __name__ == '__main__':
    unittest.main()
