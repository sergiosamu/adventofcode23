import unittest
from src.day4.main import Scratchcards 

class ScratchcardsTest (unittest.TestCase):   

    def test_processPointsTestInput(self):
        scratchcards = Scratchcards("tests/day4/testinput.txt")
        
        result = scratchcards.calculatePoints()
        self.assertEqual(result,13)     

    def test_processScratchcardsTestInput(self):
        scratchcards = Scratchcards("tests/day4/testinput.txt")
        
        result = scratchcards.countScratchcards()
        self.assertEqual(result,30)           

if __name__ == '__main__':
    unittest.main()