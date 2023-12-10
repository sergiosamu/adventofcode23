import re

class GearRatios:   

   REGEX_ONLY_SYMBOLS=r"[^.^\w^\s]"

   def __init__(self,filePath:str) -> None:
      with open(filePath, "r") as file:
         self.lines = file.readlines()
         self.lineWidth = len(self.lines[0])

   def processPartsSum(self):
      sum=0

      for idx,_ in enumerate(self.lines):
         sum+=self._processLineParts(idx)
      
      return sum
   
   def processGearRatiosSum(self):
      sum=0

      for idx,line in enumerate(self.lines):
         for pos in self._getAsterisksPositions(line):
            sum += self._getGearRatioValue(idx,pos) 

      return sum
   
   def _getAsterisksPositions(self,line:str):
      symbolPoslist = []

      symbolPos = line.find("*")
      while symbolPos != -1:
         pos = symbolPos +1
         symbolPoslist.append(symbolPos)
         symbolPos = line.find("*",symbolPos+1)
      
      return symbolPoslist
   
   def _getGearRatioValue(self,idx:int,symbolPos:int):
      result = 0
      
      numsAbove= re.split("[^\d]",self.lines[idx-1][symbolPos-1:symbolPos+2])
      numsBelow= re.split("[^\d]",self.lines[idx+1][symbolPos-1:symbolPos+2])
      numRight=self.lines[idx][symbolPos+1] if self.lines[idx][symbolPos+1].isdigit() else None
      numLeft=self.lines[idx][symbolPos-1] if self.lines[idx][symbolPos-1].isdigit() else None

      totalNums = len([x for x in numsAbove if x.isdigit()]) + len([x for x in numsBelow if x.isdigit()])
      totalNums += 1 if numRight!=None else 0
      totalNums += 1 if numLeft!=None else 0
         
      if totalNums == 2:
         numList=[]         
         if numRight != None:
            numList.append(self._getCompleteNum(idx,symbolPos+1))
         if numLeft != None:
            numList.append(self._getCompleteNum(idx,symbolPos-1))

         pos = 0
         for num in numsAbove:
            if (num.isdigit()):
               while not self.lines[idx-1][symbolPos-1+pos].isdigit():
                  pos+=1
               numList.append(self._getCompleteNum(idx-1,symbolPos-1+pos))
               pos+=1
         
         pos = 0
         for num in numsBelow:
            if (num.isdigit()):
               while not self.lines[idx+1][symbolPos-1+pos].isdigit():
                  pos+=1
               numList.append(self._getCompleteNum(idx+1,symbolPos-1+pos))
               pos+=1

         result = numList[0]*numList[1]
      
      return result 
   
   def _getCompleteNum(self,row,column):
      start = column
      end = column

      while self.lines[row][start-1].isdigit():
         start-=1
      
      while self.lines[row][end+1].isdigit():
         end+=1

      return int(self.lines[row][start:end+1])
        
   def _processLineParts(self,lineNumber:int) -> int:
      partSum = 0
      line = self.lines[lineNumber]
      numberList = re.findall(r'\d+', line)
      if len(numberList) == 0:
         return 0
      startIndex=0
      for number in numberList:  
         numberIndex=line.index(number,startIndex)
         adjacentChars = self._getSymbolsString(lineNumber,numberIndex,numberIndex+len(number))
         if re.search(self.REGEX_ONLY_SYMBOLS,adjacentChars):
            partSum+=int(number)

         startIndex=numberIndex+len(number)

      return partSum

   def _getSymbolsString(self,lineNumber:int,startIndex:int,endIndex:int):

      resultString = ""
      lineStart = startIndex if startIndex==0 else startIndex-1
      lineEnd = endIndex if endIndex==self.lineWidth-1 else endIndex+1

      if lineNumber != 0:
         resultString += self.lines[lineNumber-1][lineStart:lineEnd]         
      if lineNumber != len(self.lines)-1:
         resultString += self.lines[lineNumber+1][lineStart:lineEnd]

      if startIndex>0:
         resultString += self.lines[lineNumber][lineStart:lineStart+1]

      if endIndex<self.lineWidth-1:         
         resultString += self.lines[lineNumber][lineEnd-1:lineEnd]
      
      return resultString
                       
if __name__ == '__main__':
   gearRatios=GearRatios("src/day3/day3input.txt")
   print(gearRatios.processPartsSum())
   print(gearRatios.processGearRatiosSum())

       
    
        

        

