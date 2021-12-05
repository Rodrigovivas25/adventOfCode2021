import filesUtility as fu
from enum import Enum

class RatingType(Enum):
    OXYGEN = 1
    CO2 = 2

test = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
listOfElements = fu.getListFromFile("dayThreeElements.txt")

gammaRateBitsList = []
epsilonRateBitsList = []

def getListOfBits(elements):
    lengthOfNumbers = len(elements[0])    
    for position in range(lengthOfNumbers):
        zeroBits, oneBits = countCommonBits(position, elements)
        compareBitsAndPopulateRates(zeroBits, oneBits)

def compareBitsAndPopulateRates(zeroBits, oneBits):
    global gammaRateBitsList
    global epsilonRateBitsList

    if oneBits > zeroBits:
        gammaRateBitsList.append(1)
        epsilonRateBitsList.append(0)
    else:
        gammaRateBitsList.append(0)
        epsilonRateBitsList.append(1)

def countCommonBits(position, elements):
    zeroBits = 0
    oneBits = 0
    for number in elements:
        if number[position] == "1":
            oneBits += 1
        else:
            zeroBits += 1
    
    return zeroBits, oneBits

def getLifeSupportRating(testList, type):
    position = 0
    while len(testList) != 1:
        testList = iterateToFindSupportRating(testList, type, position)
        position += 1

    return testList[0]

def iterateToFindSupportRating(testList, type, position):
    tempList = []
    zeroBits, oneBits = countCommonBits(position, testList)
    bitOfInterest = getBitOfInterest(zeroBits, oneBits, type)
    for number in testList:
        if number[position] == bitOfInterest:
            tempList.append(number)
    
    return tempList[:]

def getBitOfInterest(zeroBits, oneBits, type):
    if oneBits > zeroBits:
        bitOfInterest = "1" if type == RatingType.OXYGEN else "0"
    elif oneBits < zeroBits:
        bitOfInterest = "1" if type == RatingType.CO2 else "0"
    else:
        bitOfInterest = "1" if type == RatingType.OXYGEN else "0"

    return bitOfInterest

def convertBinaryListToDecimal(bitsList):
    bitsString = "".join(map(str, bitsList))
    bits = int(bitsString, 2)
    return bits

def multiplyRates(gamma, epsilon):
    return gamma * epsilon


if __name__ == '__main__':
    getListOfBits(listOfElements)
    gammaRate = convertBinaryListToDecimal(gammaRateBitsList)
    epsilonRate = convertBinaryListToDecimal(epsilonRateBitsList)
    print("gammaRate binary: {0}".format(gammaRateBitsList))
    print("gammaRate decimal: {0}".format(gammaRate))
    print("epsilonRate binary: {0}".format(epsilonRateBitsList))
    print("epsilonRate decima: {0}".format(epsilonRate))
    print("multiplication: {0}".format(multiplyRates(gammaRate, epsilonRate)))
    #Part 2
    oxygen = int(getLifeSupportRating(listOfElements[:], RatingType.OXYGEN),2)
    co = int(getLifeSupportRating(listOfElements[:], RatingType.CO2),2)
    print("Oxygen: {0}".format(oxygen))
    print("CO: {0}".format(co))
    print("Oxygen * CO: {0}".format(oxygen * co))