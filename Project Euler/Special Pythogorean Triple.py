import math

#Find pythagorean triples
def findTripleProduct():

    #Iterate through all a
    for a in range(1,1000):

        #Iterate through all b (b > a)
        for b in range(a+1,1000):

            #Define c and check if it is a whole number
            c = math.sqrt((a**2)+(b**2))
            if c.is_integer():

                #Check if a+b+c = 100, if so return product
                if a+b+c == 1000:
                    return a*b*c
                
print(findTripleProduct())
