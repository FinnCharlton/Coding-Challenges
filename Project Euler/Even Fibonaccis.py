#Create Fibonacci List
list = [0,1]
while list[-1] < 4000000:
    list.append(list[-1]+list[-2])
list.remove(list[-1])

#Sum even numbered terms
sum = 0
for item in list:
    if item%2 == 0:
        sum += item


print(sum)
