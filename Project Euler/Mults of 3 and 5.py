#Create List of multiples of 3 and 5
listVar = []
for i in range(1000):
    if (i%3 ==0 or i%5 == 0) and i!=0:
        listVar.append(i)

#Sum List
sum = 0
for item in listVar:
    sum += item

print(sum)