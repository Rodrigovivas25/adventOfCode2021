import filesUtility as fu
measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def countIncreases(measurementList):
	increases = 0
	for index in range(1,len(measurementList)):
		isHigher = measurementList[index-1] < measurementList[index]
		increases = increases + 1 if isHigher else increases
	
	return increases

def getListOfSums(numbersList):
	sumList = []
	for index in range(len(numbersList)-2):
		sum = numbersList[index] + numbersList[index+1] + numbersList[index+2]
		sumList.append(sum)
	return sumList
	

if __name__ == '__main__':
	numbersList = list(map(lambda x: int(x), fu.getListFromFile("dayOneElements.txt")))
	#print(numbersList)
	#print(getListOfSums(measurements))
	sumsList = getListOfSums(numbersList)
	numberOfIncreases = countIncreases(sumsList)
	print(numberOfIncreases)


