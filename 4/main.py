def parseInput(filename):
    inputList = []
    with open(filename, 'r') as file:
        for line in file:
            inputList.append(list(line.strip()))
    return inputList

def findXmas(inputList):
    result = 0
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if inputList[i][j] == 'X':
                # Check horizontally to the right
                if j+3 < len(inputList[i]) and inputList[i][j+1] == 'M' and inputList[i][j+2] == 'A' and inputList[i][j+3] == 'S':
                    result += 1
                # Check horizontally to the left
                if j-3 >= 0 and inputList[i][j-1] == 'M' and inputList[i][j-2] == 'A' and inputList[i][j-3] == 'S':
                    result += 1
                # Check vertically downwards
                if i+3 < len(inputList) and inputList[i+1][j] == 'M' and inputList[i+2][j] == 'A' and inputList[i+3][j] == 'S':
                    result += 1
                # Check vertically upwards
                if i-3 >= 0 and inputList[i-1][j] == 'M' and inputList[i-2][j] == 'A' and inputList[i-3][j] == 'S':
                    result += 1
                # Check diagonally to the top left
                if i-3 >= 0 and j-3 >= 0 and inputList[i-1][j-1] == 'M' and inputList[i-2][j-2] == 'A' and inputList[i-3][j-3] == 'S':
                    result += 1
                # Check diagonally to the top right
                if i-3 >= 0 and j+3 < len(inputList[i]) and inputList[i-1][j+1] == 'M' and inputList[i-2][j+2] == 'A' and inputList[i-3][j+3] == 'S':
                    result += 1
                # Check diagonally to the bottom left
                if i+3 < len(inputList) and j-3 >= 0 and inputList[i+1][j-1] == 'M' and inputList[i+2][j-2] == 'A' and inputList[i+3][j-3] == 'S':
                    result += 1
                # Check diagonally to the bottom right
                if i+3 < len(inputList) and j+3 < len(inputList[i]) and inputList[i+1][j+1] == 'M' and inputList[i+2][j+2] == 'A' and inputList[i+3][j+3] == 'S':
                    result += 1
                
    return result

def find_x_mas(inputList):
    result = 0
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if inputList[i][j] == 'A':
                # Check diagonally top left to bottom right
                if i-1 >=0 and j-1 >= 0 and i+1 < len(inputList) and j+1 < len(inputList[i]) and inputList[i-1][j-1] == 'M' and inputList[i+1][j+1] == 'S':
                    # result += 1
                    # Check diagonally top right to bottom left
                    if i-1 >=0 and j+1 < len(inputList[i]) and i+1 < len(inputList) and j-1 >= 0 and inputList[i-1][j+1] == 'M' and inputList[i+1][j-1] == 'S':
                        result += 1
                
                if i-1 >=0 and j-1 >= 0 and i+1 < len(inputList) and j+1 < len(inputList[i]) and inputList[i-1][j-1] == 'S' and inputList[i+1][j+1] == 'M':
                    # result += 1
                    # Check diagonally top right to bottom left
                    if i-1 >=0 and j+1 < len(inputList[i]) and i+1 < len(inputList) and j-1 >= 0 and inputList[i-1][j+1] == 'S' and inputList[i+1][j-1] == 'M':
                        result += 1
                    # result += 1
                
                if i-1 >=0 and j-1 >= 0 and i+1 < len(inputList) and j+1 < len(inputList[i]) and inputList[i-1][j-1] == 'M' and inputList[i+1][j+1] == 'S':
                    # result += 1
                    # Check diagonally top right to bottom left
                    if i-1 >=0 and j+1 < len(inputList[i]) and i+1 < len(inputList) and j-1 >= 0 and inputList[i-1][j+1] == 'S' and inputList[i+1][j-1] == 'M':
                        result += 1
                
                if i-1 >=0 and j-1 >= 0 and i+1 < len(inputList) and j+1 < len(inputList[i]) and inputList[i-1][j-1] == 'S' and inputList[i+1][j+1] == 'M':
                    # result += 1
                    # Check diagonally top right to bottom left
                    if i-1 >=0 and j+1 < len(inputList[i]) and i+1 < len(inputList) and j-1 >= 0 and inputList[i-1][j+1] == 'M' and inputList[i+1][j-1] == 'S':
                        result += 1
                
                
    return result

def main():
    inputList = parseInput('input.txt')
    xmas = findXmas(inputList)
    x_mas = find_x_mas(inputList)
    print(xmas)
    print(x_mas)

if __name__ == '__main__':
    main()