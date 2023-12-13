#Import Packages
import urllib.request as url

#Function: Download Input Data
def urlRequest(link,cookie):
    linkRequest = url.Request(link,data=None,headers = {"cookie":"session="+ cookie})
    openRequest = url.urlopen(linkRequest)
    file = openRequest.read()
    return file

input = urlRequest("https://adventofcode.com/2023/day/1/input","53616c7465645f5f8554d18fc61bbe163e06a7097217f523db83b634b2070feda9589040193e4c1c07ff9b74c27e992768457da054560cf55d569decf8a788c5")

#Turn input data to list
inputList = str(input).split('\\')

#Forward and Backward Dictionaries:
replacementsForward = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
    }

replacementsBackward = {}
for key,value in replacementsForward.items():
    replacementsBackward.update({key[::-1]:value})

#Function: Replace characters with letters.
#Required to replace left to right
def letterReplace(string,dict):
    newString = string
    for i in range(len(string)):
        for key,value in dict.items():
            newString = newString[0:(i)].replace(key,value) + newString[i:]
    return newString

#Function: New Lists with first and last digits
def firstAndLastDigitsPartOne(list):
    output = []
    for item in list:
        for letter in item:
            if letter.isnumeric():
                firstDigit = letter
                break
        for letter in item[::-1]:
            if letter.isnumeric():
                lastDigit = letter
                break
        output.append(firstDigit + lastDigit)
    return output

#Function: New List with first and last digits
def firstAndLastDigitsPartTwo(list):
    output = []
    for item in list:
        for letter in letterReplace(item,replacementsForward):
            if letter.isnumeric():
                firstDigit = letter
                break
        for letter in letterReplace(item[::-1],replacementsBackward):
            if letter.isnumeric():
                lastDigit = letter
                break
        output.append(firstDigit + lastDigit)
    return output

#Function: Sum of List
def listSum(list):
    sum = 0
    for item in list:
        sum += int(item)
    return sum

# Get Part One Answer
print(
    "Part One Answer: " + str(listSum(firstAndLastDigitsPartOne(inputList)))
)

#Get Part Two Answer
print(
    "Part Two Answer: " + str(listSum(firstAndLastDigitsPartTwo(inputList)))
)

    
