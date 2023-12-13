#Import Packages
import urllib.request as url
import itertools as iter
from itertools import permutations
import time

#Function: Download Input Data
def urlRequest(link,cookie):
    linkRequest = url.Request(link,data=None,headers = {"cookie":"session="+ cookie})
    openRequest = url.urlopen(linkRequest)
    file = openRequest.read()
    return file

input = urlRequest("https://adventofcode.com/2023/day/12/input","53616c7465645f5f8554d18fc61bbe163e06a7097217f523db83b634b2070feda9589040193e4c1c07ff9b74c27e992768457da054560cf55d569decf8a788c5")
# practiceInput = "???.### 1,1,3\\n.??..??...?##. 1,1,3\\n?#?#?#?#?#?#?#? 1,3,1,6\\n????.#...#... 4,1,1\\n????.######..#####. 1,6,5\\n?###???????? 3,2,1"
#Form Input List Hierarchy
# print(practiceInput)
inputList = str(input).split('\\n')

def formInnerList(x):
    output =[]
    for item in x:
        output.append(item.split())
    return output

inputList2 = formInnerList(inputList)

def formInnerList2(y):
    output = []
    for list in y:
        newList = [list[0],list[-1].split(',')]
        output.append(newList)
    return output

inputList3 = formInnerList2(inputList2)


inputList3.pop() 


practiceStringTrue = '#####.#.##.#....#..'
practiceStringFalse = '###.###.#####.###..'
practiceStringInput = '###?#?#.???#?.??#..'
practiceList = ['5', '1', '2', '1', '1']

practiceString2 = '???.###'
practiceList2 = ['1','1','3']


        
def findNextHashIndex(string):
    for i in range(len(string)):
        if string[i] == '#':
            return i
    return 0
        
# print(findNextQIndex(practiceString))


".###.......#"

def checkSolution(string,testList):
    indexUp = findNextHashIndex(string)
    for i in range(len(testList)):
        # print("indexUp = " + str(indexUp) + " indexUp + int(testList[i]) = " + str(indexUp + int(testList[i])))
        if indexUp >= len(string):
            return False
        if '.' in string[indexUp:indexUp + int(testList[i])]:
            return False
        if indexUp + int(testList[i]) < len(string):
            if string[indexUp + int(testList[i])] != '.':
                return False
        if i == len(testList)-1 and '#' in string[(indexUp + int(testList[i])):]:
            return False
        indexUp += int(testList[i]) + findNextHashIndex(string[(indexUp + int(testList[i])):])
    return True


def listQs(string):
    output = []
    for i in range(len(string)):
        if string[i] == '?':
            output.append(i)
    return output

appendList = ['.','#']

def testAllCombs(string,testList):
    arrangementCount = 0
    QLocations = listQs(string)
    uniqueCombinations = []
    uniqueCombinations = list(list(zip(QLocations, element))
                           for element in iter.product(appendList, repeat = len(QLocations))
                           )
    testStringAsList = list(string)
    for x in uniqueCombinations:
        for tuple in x:
            testStringAsList[tuple[0]] = tuple[1]
        testStringAsString = ''.join(testStringAsList)
        # print(testStringAsString, testList)
        if checkSolution(testStringAsList,testList) == True:
            arrangementCount += 1
            # print("True",testStringAsString,testList)
        else:
            continue
    print(string,testList,arrangementCount)
    return arrangementCount


def testAllRows(testList):
    total = 0
    for innerList in testList:
        total += testAllCombs(innerList[0],innerList[-1])
    return total

start_time = time.time()
print(testAllRows(inputList3))
print("--- %s seconds ---" % (time.time() - start_time))

