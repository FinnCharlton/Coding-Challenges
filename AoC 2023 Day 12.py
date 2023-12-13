#Import Packages
import urllib.request as url
import itertools as iter
from itertools import permutations

#Function: Download Input Data
def urlRequest(link,cookie):
    linkRequest = url.Request(link,data=None,headers = {"cookie":"session="+ cookie})
    openRequest = url.urlopen(linkRequest)
    file = openRequest.read()
    return file

input = urlRequest("https://adventofcode.com/2023/day/12/input","53616c7465645f5f8554d18fc61bbe163e06a7097217f523db83b634b2070feda9589040193e4c1c07ff9b74c27e992768457da054560cf55d569decf8a788c5")

#Form Input List Hierarchy

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

maxCount = 0
for item in inputList:
    count = 0
    for letter in item:
        if letter == '?':
            count += 1
    if count > maxCount:
        maxCount = count

print(2**19)


# practiceStringTrue = '#####.#.##.#....#..'
# practiceStringFalse = '###.###.#####.###..'
# practiceStringInput = '###?#?#.???#?.??#..'
# practiceList = ['5', '1', '2', '1', '1']

# practiceString2 = '???.###'
# practiceList2 = ['1','1','3']
        
# def findNextHashIndex(string):
#     for i in range(len(string)):
#         if string[i] == '#':
#             return i
#     return 0
        
# # print(findNextQIndex(practiceString))


# def checkSolution(string,list):
#     indexUp = 0
#     for item in list:
#         print(indexUp)
#         if '.' in string[indexUp:indexUp + int(item)]:
#             return False
#         elif string[indexUp + int(item)] != '.':
#             return False
#         indexUp += int(item) + findNextHashIndex(string[(indexUp + int(item)):])
#     return True


# def listQs(string):
#     output = []
#     for i in range(len(string)):
#         if string[i] == '?':
#             output.append(i)
#     return output

# appendList = ['.','#']

# def testAllCombs(string,testList):
#     arrangementCount = 0
#     QLocations = listQs(string)
#     uniqueCombinations = []
#     uniqueCombinations = list(list(zip(QLocations, element))
#                            for element in iter.product(appendList, repeat = len(QLocations))
#                            )
#     testStringAsList = list(string)
#     for x in uniqueCombinations:
#         for tuple in x:
#             testStringAsList[tuple[0]] = tuple[1]
#         testStringAsString = ''.join(testStringAsList)
#         print(testStringAsString)
#         if checkSolution(testStringAsList,testList) == True:
#             arrangementCount += 1
#             print(True)
#         else:
#             print(False)
#             continue
#     return arrangementCount

# # print(testAllCombs(practiceStringInput,practiceList))
# print(testAllCombs(practiceStringInput,practiceList))