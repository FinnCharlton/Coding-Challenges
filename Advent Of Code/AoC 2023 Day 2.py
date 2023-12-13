#Import Packages
import urllib.request as url

#Function: Download Input Data
def urlRequest(link,cookie):
    linkRequest = url.Request(link,data=None,headers = {"cookie":"session="+ cookie})
    openRequest = url.urlopen(linkRequest)
    file = openRequest.read()
    return file

input = urlRequest("https://adventofcode.com/2023/day/2/input","53616c7465645f5f8554d18fc61bbe163e06a7097217f523db83b634b2070feda9589040193e4c1c07ff9b74c27e992768457da054560cf55d569decf8a788c5")

inputList = str(input).split('\\n')

def makeOuterDict(list):
    output = []
    for item in list:
        output.append({item.split(':')[0]:item.split(':')[-1]})
    return output

inputDict = makeOuterDict(inputList)

newList = []
def makeInnerList(list):
    for item in list:
        for key,value in item.items():
            newValue = value.split(';')
            newList.append({key:newValue})
    return newList

def makeInnerList2(list):
    for item in list:
        newList2
        for key,value in item.items():
            for j in value.split(','):

                dict(j)


print(makeInnerList(inputDict))

