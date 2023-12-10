import unittest
from src.day3.main import GearRatios

class GearRatiosTest(unittest.TestCase):   

    def test_processFirstLine(self):
        gearRatios = GearRatios("src/day3/day3input.txt")
        gearRatios.lines = ["467..114..",
                            "...*......",
                            "..35..633."]
        gearRatios.lineWidh = 10
        
        result = gearRatios.processLineParts(0)
        self.assertEqual(result,467)

    def test_processMidLine(self):
        gearRatios = GearRatios("src/day3/day3input.txt")
        gearRatios.lines = ["467..114..",
                            "...*......",
                            "..35..633."]
        gearRatios.lineWidh = 10
        
        result = gearRatios.processLineParts(1)
        self.assertEqual(result,0)

    def test_processLastLine(self):
        gearRatios = GearRatios("src/day3/day3input.txt")
        gearRatios.lines = ["467..114..",
                            "...*......",
                            "..35..633."]
        gearRatios.lineWidh = 10
        
        result = gearRatios.processLineParts(2)
        self.assertEqual(result,35)    

    def test_processRepeatedNumbers(self):
        gearRatios = GearRatios("src/day3/day3input.txt")
        gearRatios.lines = ["...........",
                            "..778.77...",
                            "......*...."]
        gearRatios.lineWidh = 11
        result = gearRatios.processPartsSum()
        self.assertEqual(result,77)    

    def test_testInput(self):
        gearRatios = GearRatios("tests/day3/testinput.txt")
        
        result = gearRatios.processPartsSum()
        self.assertEqual(result,4361)

    def test_processGearRatios(self):
        gearRatios = GearRatios("tests/day3/testinput.txt")
        gearRatios.lines = ["467..114..",
                            "...*......",
                            "..35..633."]
        gearRatios.lineWidh = 10
        
        result = gearRatios.processGearRatiosSum()
        self.assertEqual(result,16345)    

    def test_processGearRatios2(self):
        gearRatios = GearRatios("tests/day3/testinput.txt")
        gearRatios.lines = [".712.996..",
                            "....*.....",
                            ".........."]
        gearRatios.lineWidh = 10
        
        result = gearRatios.processGearRatiosSum()
        self.assertEqual(result,709152)                     

    def test_testInputGearRatios(self):
        gearRatios = GearRatios("tests/day3/testinput.txt")
        
        result = gearRatios.processGearRatiosSum()
        self.assertEqual(result,467835)         

if __name__ == '__main__':
    unittest.main()