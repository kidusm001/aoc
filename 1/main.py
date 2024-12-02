def readFile(filename):
    leftList = []
    rightList = []
    with open(filename, 'r') as file:
        for line in file:
            left, right = line.strip().split()
            leftList.append(int(left))
            rightList.append(int(right))
    leftList.sort() 
    rightList.sort()
    return leftList, rightList

def findDistance(leftList, rightList):
    disList = []
    for i in range(len(leftList)):
        distance = abs(leftList[i] - rightList[i])
        disList.append(distance)
    return sum(disList)

def similarityScore(leftList, rightList):
    score = 0
    scoreList = []
    for i in range(len(leftList)):
        count = rightList.count(leftList[i])
        scoreList.append(leftList[i] * count)
    score = sum(scoreList)
    return score

def main():
    leftList, rightList = readFile('input.txt')
    distance = findDistance(leftList, rightList)
    score = similarityScore(leftList, rightList)
    print(distance)
    print(score)

if __name__ == '__main__':
    main()