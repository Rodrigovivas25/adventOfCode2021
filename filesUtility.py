def getListFromFile(fileName):
	file = open(fileName, "r")
	numbersList = file.read().split("\n")
	file.close()
	return numbersList