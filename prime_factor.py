import math
import logging
logging.basicConfig(level=logging.DEBUG)

#Çarpanları bulma
def getFactors(number):
    factors = []
    for potential_factors in range (1,int(math.sqrt(number))+1):
        if number % potential_factors == 0:
            factors.append(potential_factors)
            factors.append(number / potential_factors)
    return factors
#logging.debug(getFactors(17))

#Sayının asal olup olmadığını değerlendirme
def isPrime(number):
    return len(getFactors(number)) == 2

#logging.debug('isPrime(24) = %s' % (isPrime(24)))
#logging.debug('isPrime(24) = %s' % (isPrime(17)))

#En büyük rakamı bulma
allFactors = getFactors(600851475143)
largestPrimeFactor = 0
for factor in allFactors:
    if isPrime(factor) and factor > largestPrimeFactor:
        largestPrimeFactor = factor

print(largestPrimeFactor)