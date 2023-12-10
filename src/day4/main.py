import re

class Scratchcards:   

   REGEX_ONLY_SYMBOLS=r"[^.^\w^\s]"

   def __init__(self,filePath:str) -> None:
      with open(filePath, "r") as file:
         self.lines = file.readlines()

   def calculatePoints(self):
      sum=0

      for line in self.lines:
         winningPoints=self._getLinePoints(line.split(":")[1])
         if winningPoints > 0:
            sum+=2 ** (winningPoints-1)
      
      return sum
   
   def _getLinePoints(self,line:str):
      numberList=[int (num) for num in line.split("|")[0].strip().split(" ") if num.isdigit()]
      winningNumbers=[int (num) for num in line.split("|")[1].strip().split(" ") if num.isdigit()]

      sum = 0
      for winningNum in winningNumbers:
         if winningNum in numberList:
            sum+=1   
            
      return sum   
   
   def countScratchcards(self):
      sum=0      
      winningCards = {}

      for idx in range(1,len(self.lines)+1):         
         winningCards[idx]=1
      
      print(winningCards)
      
      for idx,line in enumerate(self.lines):
         cardId=idx+1
         winningPoints=self._getLinePoints(line.split(":")[1])
         print("{} winning points {}",winningPoints)
         if winningPoints > 0:
            factor = winningCards[cardId]
            print ("{} a {}",cardId+1,cardId+winningPoints)
            print("\t factor {}",factor)
            for card in range(cardId+1,cardId+1+winningPoints):
               winningCards[card]=winningCards[card]+factor if card in winningCards else factor
               print ("\t {}",winningCards)

      for key in winningCards:
         sum+=winningCards[key]
                 
      return sum
                          
if __name__ == '__main__':
   scratchcards=Scratchcards("src/day4/day4input.txt")
   print(scratchcards.calculatePoints())
   print(scratchcards.countScratchcards())



