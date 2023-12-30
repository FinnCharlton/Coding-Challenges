import math

#Make prime list, stop when max value is 2 million
primes = [2]
i = 3
while max(primes) < 2000000:
    print(max(primes))
    checker = True
    for item in primes:
        if item < math.sqrt(i):
            if i % item == 0:
                checker = False
                break
    # print(f"i={i},checker={checker}")
    if checker == True:
        primes.append(i)
    i += 2

primes.pop()

sum = 0
for item in primes:
    sum += item

print(sum)