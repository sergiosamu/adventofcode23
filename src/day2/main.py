import re

class CubeConundrum:   
     LINE_EXPRESSION_GAME = r"Game\s(\d*)"
     LINE_EXPRESSION_MOVE = r"\s(?P<green>\d*)\sgreen|\s(?P<red>\d*)\sred|\s(?P<blue>\d*)\sblue"

     def getLineInfo(self,line:str)-> dict:        
        game=0; redCount=0; greenCount=0; blueCount=0         
        
        parts = line.split(":")        
        game = int(re.search(self.LINE_EXPRESSION_GAME,parts[0]).group(1))
        for move in parts[1].split(";"):
            for match in re.finditer(self.LINE_EXPRESSION_MOVE,move):
                if match.group("red") != None and int(match.group("red")) > redCount:
                    redCount = int(match.group("red"))
                if match.group("green") != None and int(match.group("green")) > greenCount:
                    greenCount = int(match.group("green"))
                if match.group("blue") != None and int(match.group("blue")) > blueCount:
                    blueCount = int(match.group("blue"))

        return {'game':game,'red':redCount,'green':greenCount,"blue":blueCount}

     def getGameSum(self,filePath:str,maxRed:int,maxGreen:int,maxBlue:int):
        result=0

        with open(filePath, 'r') as file:
            for line in file.readlines():
                lineInfo = self.getLineInfo(line)
                if (lineInfo["red"] <= maxRed and 
                    lineInfo["green"] <= maxGreen and 
                    lineInfo["blue"] <= maxBlue):
                    result+=lineInfo["game"]
        
        return result
     
     def getGamePower(self,filePath:str,maxRed:int,maxGreen:int,maxBlue:int):
        result=0

        with open(filePath, 'r') as file:
            for line in file.readlines():
                lineInfo = self.getLineInfo(line)
                result+=lineInfo["red"]*lineInfo["green"]*lineInfo["blue"]
        
        return result     
                    
if __name__ == '__main__':
    cubeConundrum=CubeConundrum()
    print(cubeConundrum.getGameSum("./src/day2/day2input.txt",12,13,14))
    print(cubeConundrum.getGamePower("./src/day2/day2input.txt",12,13,14))

       
    
        

        

