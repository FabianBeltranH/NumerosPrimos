import math #For the floor and sqrt functions

primeNumbersFound = 0  #Counter for prime numbers found, starts at 0 since we are also testing the number 2
currentNumber = 1 #The number we start testing with, at the beginning of the first loop it'll increment to 2

while primeNumbersFound < (10001): #We keep the loop until we find the 10001st prime number

    currentNumber = currentNumber + 1 #We begin checking if 2 is prime, then 3, etc.
    primeNumber = True #We assume all numbers are prime in first instance

    #Using the trial division method, it's only necessary to test a number up the square root of it so we set it as the upper limit of the range
    #For example, if we are testing the number 27 we only need to test up to 6~ to know if it's a prime number or not
    upperLimit = math.floor(math.sqrt(currentNumber)) + 1

    for i in range(2, upperLimit): #We compare all numbers from 2 up to the upper limit we calculated earlier

        if ((currentNumber % i) == 0): #If any of the numbers in the counter is a multiple of our current number, it means it isn't a prime number
            primeNumber = False
            break #We skip the remaining of the loop

    if (primeNumber): #If it's a prime number, we increment our prime numbers counter
        primeNumbersFound = primeNumbersFound + 1

print('The 10001st prime number is: ' + str(currentNumber) + '.') #Once we finish we print the value of the 10001st prime number
