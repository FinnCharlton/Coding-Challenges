#Make prime list, stop when it is 10001 members long
primes = [2]
i = 3
while len(primes) < 10001:
    if len([x for x in primes if i%x ==0]) == 0:
        primes.append(i)
    i += 1

#Print last member of the list
print(max(primes))