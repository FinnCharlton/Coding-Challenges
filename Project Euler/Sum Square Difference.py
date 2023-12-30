#Find sum and sum of squares
sum = 0
sumOfSquares = 0
for i in range(1,101):
    sum += i
    sumOfSquares += i**2

#Find difference
print(sum**2 - sumOfSquares)