import filesUtility as fu

test = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

instructionsList = fu.getListFromFile("dayTwoElements.txt")

depth = 0
horizontalPos = 0
aim = 0

def processInstruction(instruction):
    global horizontalPos, depth, aim
    steps = getValueOfInstruction(instruction)
    
    if "forward" in instruction:
        horizontalPos += steps
        depth += (aim * steps)
    elif "up" in instruction:
        #depth -= steps
        aim -= steps
    else:
        #depth += steps
        aim += steps

def getValueOfInstruction(instruction):
    return int(instruction.split(" ")[1])

def calculatePosition(instructions):
    for instruction in instructions:
        processInstruction(instruction)


if __name__ == '__main__':
    calculatePosition(instructionsList)
    finalMultipliedValue = lambda depth, horizontal: depth * horizontal

    print("Depth: {0}".format(depth))
    print("Horizontal position: {0}".format(horizontalPos))
    print("Aim: {0}".format(aim))
    print(finalMultipliedValue(depth, horizontalPos))
