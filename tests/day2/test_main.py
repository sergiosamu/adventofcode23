import unittest
from src.day2.main import CubeConundrum

class CubeConundrumTest(unittest.TestCase):   
  
    def test_valid_line(self):
        cubeConundrum = CubeConundrum()
        testLine="Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        resultDict = {'game':2, 'red': 1, 'green': 3, 'blue': 4}
        self.assertDictEqual(cubeConundrum.getLineInfo(testLine),resultDict)

    def test_example_input(self):
        cubeConundrum = CubeConundrum()
        testInputFile="./tests/day2/testinput.txt"
        self.assertEqual(cubeConundrum.getGameSum(testInputFile,12,13,14),8)        

    def test_max_by_move(self):
        cubeConundrum = CubeConundrum()
        testInputFile="./tests/day2/testinput.txt"
        self.assertEqual(cubeConundrum.getGameSum(testInputFile,12,13,14),8)     

    def test_example_input_power(self):
        cubeConundrum = CubeConundrum()
        testInputFile="./tests/day2/testinput.txt"
        self.assertEqual(cubeConundrum.getGamePower(testInputFile,12,13,14),2286)              


if __name__ == '__main__':
    unittest.main()