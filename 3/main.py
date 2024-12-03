import re

def parseInput(filename):
    with open (filename, 'r') as file:
        input = file.read()
    return input

def findMulFunc(input):
    funcPattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    mulFunc = re.findall(funcPattern, input)
    result = 0
    for num1, num2 in mulFunc:
        result += int(num1) * int(num2)
    return result

def findMulFuncIfDo(input):
    mulFunc = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",input)
    doit = True
    result = 0
    for func in mulFunc:
        if func =="do()":
            doit = True
            continue
        elif func == "don't()":
            doit = False
            continue
        if doit:
            num1 , num2 = re.findall("\d{1,3}",func)
            result += int(num1) * int(num2)
    return result    

    print(mulFunc)

def main():
    input = parseInput('input.txt')
    mulFunc = findMulFunc(input)
    # print(mulFunc)
    doitres = findMulFuncIfDo(input)
    print(doitres)

if __name__ == "__main__":
    main()