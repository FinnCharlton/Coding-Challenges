
palindromes = []

#Loop through all 3 digit numbers.
for i in range(100,1000):

    #Multiply by all numbers greater than it, to not repeat calculations.
    for j in range (i,1000):
        number = i*j

        #Check if number is equal to itself reversed.
        if str(number) == str(number)[::-1]:
            palindromes.append(number)

print(max(palindromes))