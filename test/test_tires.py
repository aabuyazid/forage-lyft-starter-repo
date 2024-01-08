import unittest

from os.path import dirname, abspath, join
import sys

THIS_DIR = dirname(__file__)
CODE_DIR = abspath(join(THIS_DIR, '..'))
sys.path.append(CODE_DIR)

from serviceable.carparts.Tires import *

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.2, 0.2, 0.9, 0.89999]
        tires = CarriganTires(tire_wear)
        
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.2, 0.2, 0.3, 0.89999]
        tires = CarriganTires(tire_wear)
        
        self.assertFalse(tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.5, 0.9, 0.89999]
        tires = OctoprimeTires(tire_wear)
        
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.2, 0.2, 0.3, 0.3]
        tires = OctoprimeTires(tire_wear)
        
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
