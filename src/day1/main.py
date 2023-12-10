# This is the main file for module1

class Trebuchet:

    NUMBER_WORD = {"one":"o1e","two":"t2o","three":"t3e","four":"f4r","five":"f5e",
                   "six":"s6x", "seven": "s7n", "eight":"e8t", "nine":"n9e"}
       
    def sumCalibrationFromFile (self,inputFile):
        resultSum = 0

        with open(inputFile, 'r') as file:
            for line in file.readlines():
                resultSum+=self._getCalibration(self._num2word(line))

        return resultSum
    
    def sumCalibrationFromString (self,line:str):
        return self._getCalibration(self._num2word(line))
    
    def _num2word(self, line):
        newLine = line.lower()
        for key in self.NUMBER_WORD:
            newLine = newLine.replace(key, self.NUMBER_WORD[key])

        return newLine

    def _getCalibration(self,text:str):
        firstDigit = next(x for x in text if x.isdigit())
        lastDigit = next(x for x in text[::-1] if x.isdigit())

        return int(firstDigit + lastDigit)

if __name__ == '__main__':
    inputFile = "./src/day1/day1input.txt"
    trebuchet = Trebuchet()
    print (trebuchet.sumCalibrationFromFile(inputFile))