import unittest
from src.day1.main import Trebuchet

class TrebuchetTest(unittest.TestCase):   

   
    def test_overlapping_input(self):
        trebuchet = Trebuchet()
        self.assertEqual(trebuchet.sumCalibrationFromString("eightthree"),83)

    def test_example_input(self):
        trebuchet = Trebuchet()
        self.assertEqual(trebuchet.sumCalibrationFromFile("./tests/day1/testinput.txt"),281)

if __name__ == '__main__':
    unittest.main()