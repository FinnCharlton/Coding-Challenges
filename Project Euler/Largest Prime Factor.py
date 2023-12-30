
def primeFactors(y):
    output = []
    i = 2
    #Stop when y reaches 1
    while y > 1:
        #If i is a factor, add to output and divide by it
        while y % i == 0:
            output.append(i)
            y /= i
        #Increment i
        i += 1
    return output

print(primeFactors(600851475143))

