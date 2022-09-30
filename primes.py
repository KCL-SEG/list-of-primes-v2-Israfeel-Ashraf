"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def isPrime(numberToCheck):

    if (numberToCheck == 1): return False

    x = 1
    while x < numberToCheck:
        
        if (numberToCheck % x == 0) and (x != 1 or x == numberToCheck):
            return False

        elif (x + 1) == numberToCheck:
            return numberToCheck

        x += 1
        
    return None

def checkValidity(number_of_primes):

    if number_of_primes <= 0:
        raise ValueError()

    else:
        return None

def primes(number_of_primes):

    checkValidity(number_of_primes)
    
    list1 = []
    x = 1

    while len(list1) != number_of_primes:
        if isPrime(x) is not False:
            list1.append(x)

        x += 1
            
    
    return list1

print(primes(23))
