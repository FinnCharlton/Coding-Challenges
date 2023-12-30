#Find all primes between 1 and 20
primes = [2]
for i in range(3,21):
    if len([i for x in primes if i%x == 0]) == 0:
        primes.append(i)

#Find biggest product of each under 20
def biggestMult(x):
    for i in range(20,0,-1):
        if x**i <= 20:
            return x**i
        
mults = [biggestMult(x) for x in primes]

#Remove duplicates from list
mults = list(dict.fromkeys(mults))

#Find product of list
product = 1
for item in mults:
    product *= item

print(product)