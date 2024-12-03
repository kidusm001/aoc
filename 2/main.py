def parseInput (filename):
    inputList = []
    with open(filename, 'r') as file:
        for line in file:
            inputList.append([int(x) for x in line.strip().split()])
    return inputList

def checkMonotonicity (input):
    increasing = all(1 <= input[i+1] -input[i] <= 3 for i in range(len(input)-1))
    decreasing = all(1 <= input[i] -input[i+1] <= 3 for i in range(len(input)-1))
    return increasing or decreasing

def findMonotonicity (inputList):
    checkList = []
    for input in inputList:
        checkList.append(checkMonotonicity(input))
    return checkList

def checkSafeReports (checkList):
    safeReports = 0
    for check in checkList:
        if check:
            safeReports += 1
    return safeReports

def canBeSafeReport (input):
    if checkMonotonicity(input):
        return True
    for i in range(len(input)):
        modifiedInput = input[:i] + input[i+1:]
        if checkMonotonicity(modifiedInput):
            return True
    return False

def findAllSafeReports (inputList):
    safeReports =0
    for input in inputList:
        if canBeSafeReport(input):
            safeReports +=1
    return safeReports

def main():
    inputList = parseInput('input.txt')
    checkList = findMonotonicity(inputList)
    safeReports = checkSafeReports(checkList)
    modSafeReports = findAllSafeReports(inputList)
    print(safeReports)
    print(modSafeReports)
if __name__ == '__main__':
    main()